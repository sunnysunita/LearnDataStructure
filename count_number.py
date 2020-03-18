num=int(input("enter number: "))

def count(num):
    if num<10:
        return 1
    else:
        out=1+int(count(num/10))
        return out

print(count(num))