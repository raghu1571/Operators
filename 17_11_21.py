for i in range(4):
    for j in range(4):
        print("i=",i,"j=",j)
print("-----------------------")
for i in range(10):
    if i==7:
        print("it breaks the loop on 7")
        break
    print(i)
print("-----------------------")
for i in range(1,10):
    if i==7:
        print("it breaks the loop on 7")
        break
    print(i)
print("-----------------------")
for i in range(1,20):
    if i%2==1:
        continue
    print(i)
print("-------------------------")
for letter in "python":
    if letter=='y':
        pass
        print("the pass has been blocked")
    print('current letter:',letter)

