from cakes import Cake, CAKES
from magazine import Magazine
from orders import Order
from users import customers , Customer
from utils import ExcelExporter, PdfExporter

shop = Magazine("Kenny Cake Shop", CAKES)
shop.display_cakes()


customer = customers[0]
order = Order(customer)

order.add_cake(CAKES[0])
order.add_cake(CAKES[2])

if customer.place_order(order):
    print(f"Order ready and added by {customer.name}")
else:
    print("order failed")


pdf_exporter = PdfExporter("order_invoice.pdf")
pdf_exporter.save_to_pdf(order)


sales_data = {"Chocolate cake": 1, "Strawberry cake": 1}
excel_exporter = ExcelExporter("cake_sales.xlsx")
excel_exporter.save_to_excel(sales_data)