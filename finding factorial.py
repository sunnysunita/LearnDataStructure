import sys
sys.setrecursionlimit(3000)
num=int(input("enter number"))
def findfact(num):
    if num==0:
        return 1
    fact=num*findfact(num-1)
    return fact

print(findfact(num))