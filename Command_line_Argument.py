from sys import argv

print("The Number of Command line Arguments: ",len(argv))
print("The list os Command line Arguments: ",argv)
print("command line argument one by one: ")
for x in argv:
    print(x)
name=str(input("Enter Student Name: "))
Id=str(input("Enter Student Id: "))
sclass=bool(input("Whether student is taking class[True|False]: "))
address=str(input("Enter Student Address: "))
grade=str(input("Enter Student Grade: "))
print("Conform the Details: ")
print("name:",name)
print("Id:",Id)
print("class:",sclass)
print("address:",address)
print("grade:",grade)
for name in argv:
    print(name)
    print(len(name))
