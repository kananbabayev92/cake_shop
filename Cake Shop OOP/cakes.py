class Cake:
    def __init__(self, name, price, stock, ingredients, discount=False):
        self.name = name
        self.price = price
        self.stock = stock
        self.ingredients = ingredients
        self.discount = discount

    def add_discount(self, discount_percent):
        if self.discount == True:
            discount_amount = (self.price * discount_percent) / 100
            self.price -= discount_amount
        else:
            return "dont have discount"


CAKES = [
    Cake("Chocolate cake", 15.0, 15, 
        ["flour", "cocoa powder", "sugar", "eggs"],
        discount=True),
    Cake("Vanilla cake", 18.0, 20, 
        ["milk", "vanilla", "eggs"],
        discount=False),
    Cake("Strawberry cake", 20.0, 12, 
        ["flour", "sugar", "strawberries", "baking powder", "milk"],
        discount=True)
]

