num=int(input("Enter Your Number:"))
def convertToSingleDigit(num):
    total=0
    if(num<10):
        return num
    while(num>0):
        div=int(num%10)
        num=int(num/10)
        total=total+div
    return convertToSingleDigit(total)


print(convertToSingleDigit(num))