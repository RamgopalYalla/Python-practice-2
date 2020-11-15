age = input("enter your age: ")
#if int(age) >= 18:
 #   message = "qualified"
#else:
 #   message = "not qualified"
#print(message)

message = "qualified" if int(age) >= 18 else "not qualified"
print(message)

