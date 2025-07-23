# 아래에 코드를 작성하시오.

class Animal:
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof!'
    
class Cat(Animal):
    def speak(self):
        return 'Meow!'
    
class Flyer:
    def fly(self):
        return 'Flying'
    
class Swimmer:
    def swim(self):
        return "Swimming"
    
class Duck(Flyer, Swimmer, Animal):
    def speak(self):
        return "Quack!"
    
def make_animal_speak(instance):
    print(instance.speak())

dog1 = Dog('치와와')
cat1 = Cat('페르시안 블루')
duck1 = Duck('거위')
flyer1 = Flyer()
swimmer1 = Swimmer()

make_animal_speak(dog1)
make_animal_speak(cat1)
make_animal_speak(duck1)
print(flyer1.fly())
print(swimmer1.swim())