a=int(input("enter 1st value :"))
b=int(input("enter 2nd value :"))
c=int(input("enter 3rd value:"))

min=c if a>b and a<b and a==b else c
print("enter min value",min)
max=a if a>b and a<b and a==b else c>a and c<a and c==a and  c<b and c>b and c==b
print("enter max value",max)

print("*********")
a=int(input("enter 1st value: "))
b=int(input("enter 2nd value: "))
c=int(input("enter 3rd value: "))

min=a if a>b or a<b or a==b else c>a or c<a or c==a or c<b or c>b or c==b
print("minimum value:", min)

min=c if a>b or a<b or a==b else c
print("minimum vlaue:", min)
print("*********")
a=10
b=20
min=a if a>b else 40
print("a is greater than b",min)
min=a if a<b else 40
print("a is greater than b",min)




