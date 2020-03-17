def checkNumber(arr, x):
    l=len(arr)
    if l==1:
        if arr[0]==x:
            return True
        else:
            return False
    if arr[0] == x:
        return True
    else:
        b=arr[1:]
        return checkNumber(b,x)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')

#print(checkNumber(arr,x))