CHOCOLATE = "Chocolate cake"
VANILLA = "Vanilla cake"
STAWBERRY = "Strawberry Cake"

cakes = {
    CHOCOLATE: {
        "price": 15.0,
        "has_discount": True,
        "stock": 25,
        "ingredients": ["Flour", "Cocoa powder", "Sugar", "Eggs"]
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
        "ingredients": ["Flour", "Butter", "Strawberries", "Baking powder", "Milk"]
    }
}

CHOCO_CAKE = cakes["Chocolate cake"]
VANIL_CAKE = cakes["Vanilla cake"]
STAWB_CAKE = cakes["Strawberry Cake"]


