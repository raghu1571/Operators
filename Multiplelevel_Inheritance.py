class A :
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B :
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(A,B):
    def feature5(self):
        print("Feature 5 working")
    def feature6(self):
        print("Feature 6 working")
a1=C()
a1.feature1()
a1.feature2()
a1.feature3()
a1.feature4()
a1.feature5()
a1.feature6()