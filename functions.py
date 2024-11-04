#Built- in Library functions
y = max(56, 78, 90, 23, 12)
print(y)

x = min(67, 10, 50, 45,32)
print("The minimum value is", x)

z = pow(2, 3)
print("The result is", z)


#User-defined Functions
def greeting():
    print("Hello there!")

greeting() #calling a function

def multiply():
    num1 = 23
    num2 = 10
    print(num1*num2)

multiply()

#Parameter/ Variables and Arguments/ Values
def add(a, b, c):
    print(a + b + c)

add( 3, 4, 5)
add( 45, 60, 67)
add( 15, 30, 45)

def employee(fullname, age, position, status):
    print(fullname, age, position, status)

employee("Mark Too", 34, "CEO", "Single")
