command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.Lower() == "quit":
        break