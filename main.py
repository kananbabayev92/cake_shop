import os

import discount
import user
from products import cakes

os.system("cls") #for windows
os.system("clear") #for Macos

print("...ding..dong...\nWelcome to the Kenius chocolate shop!")  # welcomepy

client_name = input("Please enter your name: ").capitalize()  # user name

# Dialog with user
print(f"Assistant: Hello, {client_name}! How can I assist you today?")

# Cake list
print(f"{client_name}: I want to buy cakes. Which cakes do you have?")

for cake_name, cake_price in cakes.items():
    print(f"{cake_name}: {cake_price} AZN")

residual_money = user.user_wallet

# Buying
while True:
    choise = (
        input(
            (
                "Please select the cake you want to buy or \
if you want to finish the shopping write 'Exit': "
            )
        )
        .capitalize()
        .strip()
    )

    if choise in cakes:
        cake_price = cakes[choise]
        if user.total_cost + cake_price > user.user_wallet:
            print("You don't have enough money.")
            break
        # append product
        user.user_bag.append(choise)
        user.total_cost += cakes[choise]
        residual_money = user.user_wallet - user.total_cost
    #for exit
    if choise == "Exit":
        print(f"Thanks for Shoppin {client_name}")
        break
    #after shopping
    print(f"Your bag: {user.user_bag}")
    print(f"Your remaining money: {residual_money} AZN")

#add discount
print(f"Available discount codes:{discount.discounts}")
user_discount = input(f"if you have 15% discount code add: ").upper()
if user_discount in discount.discounts:
    discount_amount = (user.total_cost * 15) / 100
    final_cost = user.total_cost - discount_amount
    

# Summary of purchases
print("\nSummary of your purchases:")
print(f"Total cost: {user.total_cost} AZN")
print(f"Total cost after discount: {final_cost} AZN")
print(f"Items in your bag: {user.user_bag}")
print(f"Remaining money: {residual_money} AZN")