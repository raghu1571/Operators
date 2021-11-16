a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
list=[a,b,c]
list.sort()
print("Entered Values:",list)
print("Smallest Number: ",list[0])
print("Biggest Number: ",list[-1])
print("---------------------------")
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
if (a>b) and (a>c):
    largest_num=a
elif (b>a) and (b>c):
    largest_num=b
else:
    largest_num=c
print("The biggest of three no is:",largest_num)