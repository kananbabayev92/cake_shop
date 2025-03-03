class Cake:
    def __init__(self, name, price, stock, ingredients):
        self.name = name
        self.price = price
        self.stock = stock
        self.ingredients = ingredients
    


CAKES = [
    Cake("Chocolate cake", 15.0, 15, ["flour", "cocoa powder", "sugar", "eggs"]),
    Cake("Vanilla cake", 18.0, 20, ["milk", "vanilla", "eggs"]),
    Cake("Strawberry cake", 20.0, 12, ["flour", "sugar", "strawberries", "baking powder", "milk"])
]

