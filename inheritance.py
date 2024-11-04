#Parent Class

class Animal:
    def speak(self):
        print("Animal is speaking")

#Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()
b = Dog()

b.bark()
b.speak()
