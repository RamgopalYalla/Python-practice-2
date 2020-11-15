def message(name):
    print(f"Hi {name}")


def get_message(name):
    return f"Hi {name}"


message = get_message("Ramgopal")
file = open("content.txt", "w")
file.write(message)
