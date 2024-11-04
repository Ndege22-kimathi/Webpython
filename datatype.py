
number = 25 #int
second = 56.78 #float
text = "Hello World" #string
isPythonInteresting = True #Boolean

#Data Structures- Multiple values stored in a single variable
cars= ["toyota" "nissan" "volkswagen"] #This is a list- it is ordered, changeable
fruits = ("banana" "orange" "apple") #Tuple- Ordered but unchangeable
countries = {"Kenya" "Tunisia" "Algeria"} #This is a set and utilizes cali braces, unordered, and unchangeable
student = {
    "firstname" : "Mary",
    "age": 34,
    "course": "Web Development",
    "nationality" : "Kenyan"
} #Dictionary - Key and value pair

print(cars)
print(fruits)
print(countries)
print(student)


print(number)
print(second)
print(text)
print(isPythonInteresting)

#Determining a data type
print(type (countries))
print(type (student))

#Type-casting: process of converting frm one data type to another

print(float(number))
print(int(second))