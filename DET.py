from abc import ABC, abstractmethod

#Деталь, механизм, изделие, узел

class Detail(ABC):
    @abstractmethod
    def purpose():
        pass

class Knot(Detail):
    def __init__(self, material):
        self.material = material

    def purpose(self):
        print(f'The knot held the two pieces {self.material} together')

class Machine(Detail):
    def purpose():
        print("Make a product")

class Product(Detail):
    def __init__(self, cost):
        self.cost = cost
        
    def purpose(self):
        print(f'Usless. absoulutley usless. Its not even worth {self.cost}')
                



vase = Product("15 рубликов")
vase.purpose