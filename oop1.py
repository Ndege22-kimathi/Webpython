#Object-Oriented Programming
#A class as a blueprint of an object
#An object is  an instance of a class
from datatype import student


class Student:
    #Properties/ Characteristics/ Variables/ Attributes
    name = " Joe "
    age =- 21

    #Behaviors/ Methods/ Functions

    def study(self):
        print("Student is studying")

student1 = Student()        #Instantiating/Creating an object

student1.study()

print(student1.name)



