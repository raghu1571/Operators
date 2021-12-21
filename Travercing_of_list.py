n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(i)
    i=i+1
print("-----------------")
s="'hello welcome to besent tech"
l=s.split("w")
for hello in l:
    print(hello)
print("Set Data Type")
s={10,20,30,40,50}
print(s)
print("-----------------")
s={10,20,30,40}
i={50,60,70,80}
s.update(i,range(5))
print(s)
print("-----------------")
s={10,20,30,40}
i={50,60,70,80}
s.update(i)
print(s)
print("-----------------")
s={10,20,30,40}
s.add(50)
print(s)