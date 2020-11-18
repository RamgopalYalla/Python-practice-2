try:
    age = int(input("age: "))
    print(f" Your age is {age}")
except ValueError as ex:
    print("Please enter correct age")
    #print(ex)
    #print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues.")
