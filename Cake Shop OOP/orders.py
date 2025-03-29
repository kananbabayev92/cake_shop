class Order:
    def __init__(self, customer):
        self.customer = customer
        self.cakes = []
        self.total = 0

    def add_cake(self, cake):
        self.cakes.append(cake)
        self.total += cake.price




