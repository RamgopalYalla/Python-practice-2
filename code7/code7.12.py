class Animal:
    def __init__(self):
        print("animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammel(Animal):
    def walk(self):
        print("walk")
    def __init__(self):
        super().__init__()
        print("Mammal Constructure")
        self.weight = 2


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammel()
print(m.age)
