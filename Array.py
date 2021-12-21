from array import *

arr= array('i',[])
n= int(input("Enter The Length of an array: "))

for i in range(n):
    x=int(input("Enter Your Value: "))
    arr.append(x)

print (arr)
#print(arr[4])
print("***************Search The Value in Array**************")
print("*** By using manual code ***")
v= int(input("Enter Value for search: "))
k=0

for e in arr:
    if e==v:
        print(k)
        break
    k+=1
else:
    print("**Please Check The Vlaue You Entered**")
print("*** By using function ***")
print(arr.index(v))
