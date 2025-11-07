import logging

logging.basicConfig(filename="app.log", filemode="w",format='%(asctime)s %(message)s'
    )  
class Magazine:
    def __init__(self, title, cakes):
        self.title = title
        self.cakes = cakes

    def display_cakes(self):
        print(f"Magazine: {self.title}")
        for cake in self.cakes:
            print(f"{cake.name}: ${cake.price}")
            logging.INFO("showing cake name")


cake = Magazine("delicious cakes", [])

print(cake)

     
    
