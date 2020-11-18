try:
    file = open("app.py")
    age = int(input("age: "))
    xfactor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print("Please enter correct age")
else:
    print("No exceptions were thrown")
finally:
    file.close()
