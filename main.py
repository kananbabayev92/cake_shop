from text import USER_PROMPT
import products
import config
import user
import os
import time
import random
from fpdf import FPDF

#os.system("clear") #for Macos


SHOP_BALANCE = 0
TOTAL_SALES_CAKE = 0

start_time = time.time()
end_time = start_time + 10


while time.time() < end_time:
    print("     ...ding..dong...\nWelcome to the Kenius chocolate shop!")  
    print(f"Assistant: Hello, {random.choice(user.user_names)}! How can I assist you today?")
    print("Guest: I want to buy cakes. Which cakes do you have?\n")
    
    #show cake list
    for cake_name, cake_details in products.cakes.items():
        print(f"Cake: {cake_name}")
        print(f"Price: {cake_details['price']} AZN")
        print(f"Discount: {'Yes' if cake_details['has_discount'] else 'No'}")
        print(f"Stock: {cake_details['stock']} available")
        print(f"Ingredients: {', '.join(cake_details['ingredients'])}\n")   

    os.system("cls") #for windows

    def buy_cake(cake_name):
        global TOTAL_SALES_CAKE
        cake = products.cakes[cake_name]

        if cake["stock"] > 0:
            quantity_sold = random.randint(1, 2)

            if quantity_sold > cake["stock"]:
                quantity_sold = cake["stock"]
    
            cake["stock"]-= quantity_sold
            TOTAL_SALES_CAKE += quantity_sold
            return f"Buy {cake_name} price {cake["price"]}  AZN! in stock: {cake["stock"]}"
        else:
            return f"sorry, {cake_name} dont have! Finish shopping"
        

    cake_choice = random.choice(list(products.cakes.keys()))
    print(buy_cake(cake_choice))

    
    

    time.sleep(0.4)
    
# print("Chocolate cake", products.CHOCO_CAKE["stock"])
# print("Strawberry Cake", products.STAWB_CAKE["stock"])
# print("Vanilla cake", products.VANIL_CAKE["stock"])
# print("Total sales: ", TOTAL_SALES_CAKE)


pdf = FPDF()
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.ln(10)  # Line break

# Stock status
pdf.cell(txt=f"Chocolate Cake stock: {products.CHOCO_CAKE['stock']}", ln=True)
pdf.cell(txt=f"Strawberry Cake stock: {products.STAWB_CAKE['stock']}", ln=True)
pdf.cell(txt=f"Vanilla Cake stock: {products.VANIL_CAKE['stock']}", ln=True)
pdf.ln(10)  # Line break

# Total sales
pdf.cell(txt=f"Total cakes sold: {TOTAL_SALES_CAKE}", ln=True)

# Output the PDF to a file
pdf.output("sales_report.pdf")

