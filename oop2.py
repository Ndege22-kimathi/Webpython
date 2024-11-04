class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("Person is walking")


a = Person("Joe", 34, "Male")
print(a.name)
print(a.age)
b = Person("Mary", 24, "Female")
print(b.name)
print(b.gender)
c = Person("John", 45, "Male")
print(c.name)
print(c.gender)



