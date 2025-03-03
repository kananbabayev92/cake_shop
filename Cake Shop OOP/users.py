class Customer:
    def __init__(self, name, user_wallet):
        self.name = name
        self.user_wallet = user_wallet
        self.orders = []

    def place_order(self, order):
        if self.user_wallet >= order.total:
            self.orders.append(order)
            self.user_wallet -= order.total
            return True
        else:
            return False
        

customers = [
    Customer("Kanan", 500),
    Customer("Ayla", 300),
    Customer("Julia", 450)
]

