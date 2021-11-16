a=int(input("enter 1st value: "))
b=int(input("enter 2nd value: "))
c=int(input("enter 3rd value: "))

min=a if a<b and a<c else b if b<c else c
print("minimum value: ",min)
max=a if a>b and a>c else b if b>c else c
print("maximum value: ",max)
print("****************")
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
print("a is equal to  b"if a==b else "a is greater than b"if a>b else "a is lesser than b")