try:
    with open("app.py") as file:
        print("file opened")
    age = int(input("age: "))
    factor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print("Please enter correct age")
else:
    print("No exceptions were thrown")
finally:
    file.close()
