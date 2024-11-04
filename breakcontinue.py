#Used when there is need for breaking a sequence or skipping in the case of break

#Break Statement- Exits the entire loop
num = 20
while num <= 25:
    print(num)
    if num ==23:
        break
    num += 1

#Continue statement- skips a loop
devices = ["Laptop", "Phone", "Tablet"]
for x in devices:
    if x == "Phone" :
        continue
    print(x)    