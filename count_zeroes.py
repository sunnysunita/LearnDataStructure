num=int(input("enter number: "))
count=0
def cZero(num,count):
    if num<10:
        if num==0:
            count+=1
            return count
        else:
            return count
    if num%10==0:
        count+=1
    return cZero(int(num/10),count)

print(cZero(num,0))