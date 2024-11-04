temperature = 34

if temperature > 20:
    print("It is too hot")

else:
    print("It is too cold")

#A python program to check three numbers and return the smallest number
num1 = 67
num2 = 24
num3 = 89

if num1 < num2 and num1 < num3:
    print(num1, " is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, " is the smallest number")

else:
    print(num3, " is the smallest number")

#A python program to check three numbers and return the largest number

x = 10
y = 6
z = 19

if x > y and x > z:
    print(x, " is the largest number")

elif y > x and y > z:
    print(y, " is the largest number")

else:
    print(z, " is the largest number")

#A program to check whether a number is even or odd
number = 45

if number % 2 == 0:
    print(number, "is an even number")

else:
    print(number, " is an odd number")