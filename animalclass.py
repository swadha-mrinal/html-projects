from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk and run.")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("i can bark")
class Lion(Animal):
    def move(self):
        print("i can roar")

R = human()
R.move()
k = Snake()
k.move()
C = Dog()
C.move()
d = Lion()
d.move()