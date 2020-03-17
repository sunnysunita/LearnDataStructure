user_input=input("enter value of list: ")
list=list(map(int,user_input.split()))
x=int(input("enter value of x: "))
print(list)

def findx(list,si,x):
    l=len(list)
    if si==l:
        return -1
    smalllist=findx(list,si+1,x)
    if smalllist==-1:
        if list[si]==x:
            return si
        else:
            return -1
    else:
        return smalllist

print(findx(list,0,x))