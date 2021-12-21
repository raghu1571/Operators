a=int(input("Enter Your 1st Number: "))
b=int(input("Enter Your 2nd Number: "))

try:
    print("#Resource Open#")
    print(a/b)
    c=int(input("Enter Your Input: "))
except ZeroDivisionError as e:
    print("** Hey you cannot devide a number by zero **", e)
except ValueError as e:
    print("** Invalid Input **")
except Exception as e:
    print("** Something went wrong.... **")
finally:
    print("#Resource Closed#")
