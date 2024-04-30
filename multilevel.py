class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getAll(self):
        return self.name, self.price
class Produce(Food):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
    def getAll(self):
        return self.name, self.price, self.color

class Vegetables(Produce):
    def __init__(self,  name, price, color, type):
        super().__init__(name, price, color)
        self.type = type
    def getAll(self):
        return self.name, self.price, self.color, self.type
class Fruits(Produce):
    def __init__(self,  name, price, color, seeds):
        super().__init__(name, price, color)
        self.seeds = seeds
    def getAll(self):
        return self.name, self.price, self.color, self.seeds

vegOne = Vegetables("Pechay", 25, "green", "leafy")
print(Vegetables.getAll(vegOne))
print(Produce.getAll(vegOne))
print(Food.getAll(vegOne))

# prodOne = Produce("Banana", 30, "yellow")
# print(Produce.getAll(prodOne))
# print(Food.getAll(prodOne))
#print(Vegetables.getAll(prodOne))

prodOne = Fruits("Banana", 30, "yellow", "circles")
print(Fruits.getAll(prodOne))
print(Produce.getAll(prodOne))
print(Food.getAll(prodOne))