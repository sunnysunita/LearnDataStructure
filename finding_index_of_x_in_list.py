user_input=input("enter value of list: ")
arr=list(map(int,user_input.split()))
x=int(input("enter value of x: "))
print(arr)

def findx(arr,si,x):
    l=len(arr)
    if si==l-1 or si==l:
        if arr[si]==x:
            return si
        else:
            return -1
    if arr[si]==x:
        return si
    else:
        return findx(arr,si+1,x)

print(findx(arr,0,x))