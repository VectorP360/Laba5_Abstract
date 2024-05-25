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
        print(f'The knot held the two {self.material} pieces together\n')

class Machine(Detail):
    def __init__(self, product):
        self.product = product

    def purpose(self):
        print(f'Make a {self.product}\n')

class Product(Detail):
    def __init__(self, cost):
        self.cost = cost
        
    def purpose(self):
        print(f'Usless. absoulutley usless. Its not even cost {self.cost}\n')