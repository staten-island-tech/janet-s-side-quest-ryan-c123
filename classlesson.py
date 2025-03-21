""" class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    def add_many(list):
        print(sum(list))
        return sum(list)
    def subtract(list):
        return list

Calculator.add(9,12) """
class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant("Joanna", ['Chicken', 'Pork', 'Beef'])
print(Joanna.sell('Pork'))
Alvin = Merchant('Alvin', ['Human', "Alvin's Servitude", 'Break', 'Organs'])
print(Alvin.sell('Human'))