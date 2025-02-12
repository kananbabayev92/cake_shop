from text import USER_PROMPT
import products
import config
import user
import os
import time
import random


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

    def buy_cake(cake_name):
        cake = products.cakes[cake_name]

        if cake["stock"] > 0:
            cake["stock"] -= random.randint(1, 2) 
            return f"Buy {cake_name} price {cake["price"]}  AZN! in stock: {cake["stock"]}"
        else:
            return f"sorry, {cake_name} dont have!"
        
    os.system("cls") #for windows

    cake_choice = random.choice(list(products.cakes.keys()))
    print(buy_cake(cake_choice))
    

    time.sleep(0.4)
    
print("Chocolate cake", products.CHOCO_CAKE["stock"])
print("Strawberry Cake", products.STAWB_CAKE["stock"])
print("Vanilla cake", products.VANIL_CAKE["stock"])
print(products.cakes.items())