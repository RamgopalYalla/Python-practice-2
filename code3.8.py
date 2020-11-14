for number in range(3):
    print("loop", (number +1) * ".")

for number in range(1,4):
    print("loop",number, number * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")


for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
