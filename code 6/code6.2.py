try:
    age = int(input("age: "))
    xfactor = 10 / age
except ValueError:
    print("Please enter correct age")
else:
    print("No exceptions were thrown")
