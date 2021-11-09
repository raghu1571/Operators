a=int(input("enter 1st value :"))
b=int(input("enter 2nd value :"))
c=int(input("enter 3rd value:"))

min=c if a>b and a<b and a==b else c
print("enter min value",min)
max=a if a>b and a<b and a==b else c
print("enter max value",max)

print("*********")
a=int(input("enter 1st value: "))
b=int(input("enter 2nd value: "))
c=int(input("enter 3rd value: "))

min=a if a>b or a<b or a==b else c
print("minimum value:", min)

min=c if a>b or a<b or a==b else c
print("minimum vlaue:", min)
print("*********")