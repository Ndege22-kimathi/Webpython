try:
    print(number)
except:
    print("An error has occurred")



num1 = 39
num2 = 3


try:
    print(num1 / num2)
except:
    print("ZeroDivisionError: division by zero is impossible")

finally:
    print("Success")

