num=int(input("enter number: "))

def isArm(num):
    if num<10:
        return num*num*num
    else:
        res=((num%10)*(num%10)*(num%10))+int(isArm(int(num/10)))
        return res

print(isArm(num))
out=isArm(num)
if out==num:
    print("Armstrong Number.")
else:
    print("Not Armstrong Number.")