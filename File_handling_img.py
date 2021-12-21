A=open('Hareesh.jpg', 'rb')
for i in A:
    print(A)
A1=open('Bro.jpg', 'wb')
for i in A:
    A1.write(i)