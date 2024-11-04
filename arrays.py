#Carries Data of similar type

courses = ["MIT", "DataScience", "Cybersecurity"]
print(courses)

#Accessing an element in an array- index positions strarting from 1
print(courses [1])

#Looping through array
for y in courses:
    print("Course is", y)

#Adding a new element
courses.append("Android Development")
print(courses)

#removing an element
courses.remove("MIT")
print(courses)