def sumArray(arr):
    l=len(arr)
    if l==1:
        return arr[0]
    b=arr[1:]
    sum=arr[0]+sumArray(b)
    return sum

# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))

print(sumArray(arr))
