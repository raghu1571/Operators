a=input("Enter value of a: ")
b=input("Enter value of b: ")
c=input("Enter value of c: ")
list=[a,b,c]
print("Smallest Number: ",min(list))
print("Biggest Number: ",max(list))
print("--------------------------")
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
if (a<b) and (a<c):
    smallest_num=a
elif (b<a) and (b<c):
    smallest_num=b
else:
    smallest_num=c
print("The smallest of three no is:",smallest_num)