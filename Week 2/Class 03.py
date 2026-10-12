# Week 2 | Class 03: OOP methods, polymorphism and special methods

from abc import ABC, abstractmethod
from dataclasses import dataclass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        # Add areas to demonstrate operator overloading
        return self.area() + other.area()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:  # polymorphism
    print(type(shape).__name__, "area =", round(shape.area(), 2))

print("Combined area:", Rectangle(2, 3) + Rectangle(4, 2))

@dataclass
class ModelScore:
    model_name: str
    accuracy: float

score = ModelScore("Baseline", 0.87)
print(score)

# Public/protected/private naming convention demonstration
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._currency = "PKR"       # protected by convention
        self.__balance = balance     # name-mangled

    def get_balance(self):
        return self.__balance

account = Account("Ayesha", 5000)
print(account.owner, account._currency, account.get_balance())
