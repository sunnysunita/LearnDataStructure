num=int(input("enter number: "))

def sum(num):
    if num<10:                          #base case....
        return num
    else:
        out=num%10+int(sum(num/10))     #recusion....
        return out

print(sum(num))