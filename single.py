class Food:
    def __init__(self,  name, price):
        self.name = name
        self.price = price
    def getDetails(self):
        return self.name, self.price
class Meat(Food):
    def __init__(self,  name, price, type):
        super().__init__(name, price)
        self.type = type
    def getDetails(self):
        return self.type

foodOne = Food("adobo", 5)
meatOne = Meat("pork adobo", 10, "viand")
print(Food.getDetails(foodOne))
print(Food.getDetails(meatOne))
print(Meat.getDetails(meatOne))