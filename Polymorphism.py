class Student:
    def __init__ (self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def __add__(self, other):
        m1= self.m1 + other.m1
        m2= self.m2 + other.m2
        m3= self.m3 + other.m3

        s4= Student(m1,m2,m3)

        return s4

s1=Student(36,45,78)
s2=Student(75,80,90)
s3=Student(75,86,56)

s4=s1+s2+s3

print(s4.m1)
print(s4.m2)
print(s4.m3)