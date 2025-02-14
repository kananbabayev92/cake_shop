CHOCOLATE = "Chocolate cake"
VANILLA = "Vanilla cake"
STAWBERRY = "Strawberry Cake"

cakes = {
    CHOCOLATE: {
        "price": 15.0,
        "has_discount": True,
        "stock": 25,
        "ingredients": ["flour", "cocoa powder", "sugar", "eggs"]
    },
    VANILLA : {
        "price": 18.0,
        "has_discount": False,
        "stock": 10,
        "ingredients": ["milk", "egg","vanilla"]
    },
    STAWBERRY : {
        "price": 18,  
        "has_discount": True,
        "stock":20, 
        "ingredients": ["flour", "butter", "strawberries", "baking powder", "milk"]
    }
}

CHOCO_CAKE = cakes["Chocolate cake"]
VANIL_CAKE = cakes["Vanilla cake"]
STAWB_CAKE = cakes["Strawberry Cake"]


stocks_data =(CHOCO_CAKE["stock"], 
         VANIL_CAKE["stock"],
         STAWB_CAKE["stock"]
         )

from typing import Any

def find_max_min_stocks(stocks) -> tuple :
    min_stock = min(stocks)
    max_stock = max(stocks)
    return min_stock, max_stock

min_stock, max_stock = find_max_min_stocks(stocks)

print(type(find_max_min_stocks(stocks)))


