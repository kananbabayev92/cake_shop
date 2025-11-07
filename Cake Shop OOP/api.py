from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import os

from cakes import Cake, CAKES
from magazine import Magazine
from orders import Order
from users import customers, Customer
from utils import ExcelExporter, PdfExporter, PromoCode

app = FastAPI(
    title="Cake Shop API",
    description="A REST API for managing a cake shop with orders, customers, and exports",
    version="1.0.0"
)

# Pydantic models for request/response
class CakeResponse(BaseModel):
    name: str
    price: float
    stock: int
    ingredients: List[str]
    discount: bool

    class Config:
        from_attributes = True

class CustomerResponse(BaseModel):
    name: str
    user_wallet: float
    orders_count: int

    class Config:
        from_attributes = True

class OrderItem(BaseModel):
    cake_name: str

class CreateOrderRequest(BaseModel):
    customer_name: str
    cake_names: List[str]

class OrderResponse(BaseModel):
    customer_name: str
    cakes: List[CakeResponse]
    total: float
    status: str

class PlaceOrderRequest(BaseModel):
    customer_name: str
    order_id: Optional[int] = None

class PromoCodeRequest(BaseModel):
    promocode: str
    price: float

class PromoCodeResponse(BaseModel):
    original_price: float
    discounted_price: float
    discount_percent: float

class SalesDataRequest(BaseModel):
    sales_data: dict

# In-memory storage for orders (in production, use a database)
orders_storage = {}
order_counter = 0

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Cake Shop API",
        "version": "1.0.0",
        "endpoints": {
            "cakes": "/api/cakes",
            "customers": "/api/customers",
            "orders": "/api/orders",
            "docs": "/docs"
        }
    }

@app.get("/api/cakes", response_model=List[CakeResponse])
async def get_cakes():
    """Get all available cakes"""
    return CAKES

@app.get("/api/cakes/{cake_name}", response_model=CakeResponse)
async def get_cake(cake_name: str):
    """Get a specific cake by name"""
    cake = next((c for c in CAKES if c.name.lower() == cake_name.lower()), None)
    if not cake:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cake '{cake_name}' not found"
        )
    return cake

@app.get("/api/customers", response_model=List[CustomerResponse])
async def get_customers():
    """Get all customers"""
    return [
        CustomerResponse(
            name=customer.name,
            user_wallet=customer.user_wallet,
            orders_count=len(customer.orders)
        )
        for customer in customers
    ]

@app.get("/api/customers/{customer_name}", response_model=CustomerResponse)
async def get_customer(customer_name: str):
    """Get a specific customer by name"""
    customer = next((c for c in customers if c.name.lower() == customer_name.lower()), None)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer '{customer_name}' not found"
        )
    return CustomerResponse(
        name=customer.name,
        user_wallet=customer.user_wallet,
        orders_count=len(customer.orders)
    )

@app.post("/api/orders", response_model=OrderResponse)
async def create_order(request: CreateOrderRequest):
    """Create a new order"""
    global order_counter
    
    # Find customer
    customer = next((c for c in customers if c.name.lower() == request.customer_name.lower()), None)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer '{request.customer_name}' not found"
        )
    
    # Create order
    order = Order(customer)
    
    # Add cakes to order
    for cake_name in request.cake_names:
        cake = next((c for c in CAKES if c.name.lower() == cake_name.lower()), None)
        if not cake:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cake '{cake_name}' not found"
            )
        order.add_cake(cake)
    
    # Store order
    order_counter += 1
    orders_storage[order_counter] = order
    
    return OrderResponse(
        customer_name=order.customer.name,
        cakes=[CakeResponse(
            name=cake.name,
            price=cake.price,
            stock=cake.stock,
            ingredients=cake.ingredients,
            discount=cake.discount
        ) for cake in order.cakes],
        total=order.total,
        status="created"
    )

@app.get("/api/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int):
    """Get a specific order by ID"""
    if order_id not in orders_storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found"
        )
    
    order = orders_storage[order_id]
    return OrderResponse(
        customer_name=order.customer.name,
        cakes=[CakeResponse(
            name=cake.name,
            price=cake.price,
            stock=cake.stock,
            ingredients=cake.ingredients,
            discount=cake.discount
        ) for cake in order.cakes],
        total=order.total,
        status="placed" if order in order.customer.orders else "created"
    )

@app.post("/api/orders/{order_id}/place")
async def place_order(order_id: int):
    """Place an order (process payment)"""
    if order_id not in orders_storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found"
        )
    
    order = orders_storage[order_id]
    customer = order.customer
    
    if customer.place_order(order):
        return {
            "message": f"Order {order_id} placed successfully",
            "customer": customer.name,
            "total": order.total,
            "remaining_wallet": customer.user_wallet
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Insufficient funds. Required: ${order.total}, Available: ${customer.user_wallet}"
        )

@app.post("/api/promo/apply", response_model=PromoCodeResponse)
async def apply_promo_code(request: PromoCodeRequest):
    """Apply a promotional code to a price"""
    promo = PromoCode(True, request.promocode, 20)  # 20% discount
    discounted_price = promo.apply_promocode(request.price)
    
    return PromoCodeResponse(
        original_price=request.price,
        discounted_price=discounted_price,
        discount_percent=20.0
    )

@app.post("/api/export/pdf/{order_id}")
async def export_order_pdf(order_id: int):
    """Export an order to PDF invoice"""
    if order_id not in orders_storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found"
        )
    
    order = orders_storage[order_id]
    filename = f"order_{order_id}_invoice.pdf"
    
    pdf_exporter = PdfExporter(filename)
    pdf_exporter.save_to_pdf(order)
    
    if os.path.exists(filename):
        return FileResponse(
            filename,
            media_type="application/pdf",
            filename=filename
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate PDF"
        )

@app.post("/api/export/excel")
async def export_sales_excel(request: SalesDataRequest):
    """Export sales data to Excel file"""
    filename = "cake_sales.xlsx"
    
    excel_exporter = ExcelExporter(filename)
    excel_exporter.save_to_excel(request.sales_data)
    
    if os.path.exists(filename):
        return FileResponse(
            filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=filename
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate Excel file"
        )

@app.get("/api/shop/info")
async def get_shop_info():
    """Get shop information and available cakes"""
    shop = Magazine("Kenny Cake Shop", CAKES)
    return {
        "shop_name": shop.title,
        "total_cakes": len(shop.cakes),
        "cakes": [
            {
                "name": cake.name,
                "price": cake.price,
                "stock": cake.stock
            }
            for cake in shop.cakes
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

