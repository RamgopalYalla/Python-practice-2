try:
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter correct age")
else:
    print("No exceptions were thrown")
