class animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating.")
class Dog(animal):
    def bark(self):
        print(f"{self.name} is barking.")
class Cat(animal):
    def meow(self):
        print(f"{self.name} is meowing.")
dog=Dog("Buddy")
cat=Cat("Whiskers")
dog.eat()
dog.bark()
cat.eat()
cat.meow()
        
        
