# Cake Shop OOP

A Python object-oriented programming project that simulates a cake shop management system. This project demonstrates OOP principles with classes for cakes, customers, orders, and export utilities.

## Features

- **Cake Management**: Create and manage cakes with prices, stock, ingredients, and discount functionality
- **Customer Management**: Handle customers with wallet balance and order history
- **Order Processing**: Create orders, add cakes, and process payments
- **Export Functionality**: Export orders to PDF invoices and sales data to Excel files
- **Promo Code System**: Apply discount codes to orders

## Project Structure

```
Cake Shop OOP/
├── main.py          # Main entry point and demo
├── api.py           # FastAPI REST API endpoints
├── cakes.py         # Cake class and predefined cakes
├── magazine.py      # Magazine/Shop class for displaying cakes
├── orders.py        # Order class for managing customer orders
├── users.py         # Customer class and predefined customers
├── utils.py         # Utility classes (ExcelExporter, PdfExporter, PromoCode)
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Classes

### Cake
Represents a cake with the following attributes:
- `name`: Name of the cake
- `price`: Price of the cake
- `stock`: Available stock quantity
- `ingredients`: List of ingredients
- `discount`: Boolean indicating if discount is available

**Methods:**
- `add_discount(discount_percent)`: Applies a discount percentage to the cake price

### Magazine
Represents the cake shop/magazine.

**Methods:**
- `display_cakes()`: Displays all available cakes with their prices

### Customer
Represents a customer with wallet functionality.

**Attributes:**
- `name`: Customer name
- `user_wallet`: Available balance
- `orders`: List of placed orders

**Methods:**
- `place_order(order)`: Places an order if sufficient wallet balance is available

### Order
Represents a customer order.

**Attributes:**
- `customer`: The customer placing the order
- `cakes`: List of cakes in the order
- `total`: Total price of the order

**Methods:**
- `add_cake(cake)`: Adds a cake to the order and updates the total

### ExcelExporter
Exports sales data to Excel format.

**Methods:**
- `save_to_excel(data)`: Saves sales data dictionary to an Excel file

### PdfExporter
Exports order invoices to PDF format.

**Methods:**
- `save_to_pdf(order)`: Generates a PDF invoice for an order

### PromoCode
Handles promotional code functionality.

**Methods:**
- `apply_promocode(price)`: Applies a discount percentage to a price if promo code is active

## Installation

1. Clone or download this repository

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or if using Pipenv:
```bash
pipenv install
```

## Dependencies

- `openpyxl==3.1.5` - For Excel file generation
- `et-xmlfile==2.0.0` - Dependency for openpyxl
- `fpdf==1.7.2` - For PDF file generation
- `fastapi==0.104.1` - Modern, fast web framework for building APIs
- `uvicorn[standard]==0.24.0` - ASGI server for running FastAPI
- `python-multipart==0.0.6` - For handling form data in FastAPI

## Usage

### Running the Demo Script

Run the main script to see a demonstration:

```bash
python main.py
```

The demo will:
1. Create a cake shop and display available cakes
2. Create a customer order
3. Add cakes to the order
4. Process the order payment
5. Export the order to a PDF invoice
6. Export sales data to an Excel file

### Running the API Server

Start the FastAPI server:

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

- **Interactive API Documentation**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative API Documentation**: `http://localhost:8000/redoc` (ReDoc)

## API Endpoints

### Root
- `GET /` - API information and available endpoints

### Cakes
- `GET /api/cakes` - Get all available cakes
- `GET /api/cakes/{cake_name}` - Get a specific cake by name

### Customers
- `GET /api/customers` - Get all customers
- `GET /api/customers/{customer_name}` - Get a specific customer by name

### Orders
- `POST /api/orders` - Create a new order
  ```json
  {
    "customer_name": "Kanan",
    "cake_names": ["Chocolate cake", "Strawberry cake"]
  }
  ```
- `GET /api/orders/{order_id}` - Get order details by ID
- `POST /api/orders/{order_id}/place` - Place an order (process payment)

### Promo Codes
- `POST /api/promo/apply` - Apply a promotional code
  ```json
  {
    "promocode": "SAVE20",
    "price": 25.0
  }
  ```

### Exports
- `POST /api/export/pdf/{order_id}` - Export order to PDF invoice
- `POST /api/export/excel` - Export sales data to Excel
  ```json
  {
    "sales_data": {
      "Chocolate cake": 1,
      "Strawberry cake": 1
    }
  }
  ```

### Shop Information
- `GET /api/shop/info` - Get shop information and available cakes

### Example API Usage

**Create an order:**
```bash
curl -X POST "http://localhost:8000/api/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Kanan",
    "cake_names": ["Chocolate cake", "Strawberry cake"]
  }'
```

**Place an order:**
```bash
curl -X POST "http://localhost:8000/api/orders/1/place"
```

**Get all cakes:**
```bash
curl "http://localhost:8000/api/cakes"
```

## Example Output

When you run `main.py`, you'll see:
- Available cakes displayed from the shop
- Order confirmation message
- PDF invoice saved as `order_invoice.pdf`
- Excel sales report saved as `cake_sales.xlsx`

## Predefined Data

### Cakes
- Chocolate cake ($15.00) - with discount available
- Vanilla cake ($18.00) - no discount
- Strawberry cake ($20.00) - with discount available

### Customers
- Kanan (Wallet: $500)
- Ayla (Wallet: $300)
- Julia (Wallet: $450)

## Logging

The application logs cake display events to `app.log` file.

## License

This is a learning project for educational purposes.

