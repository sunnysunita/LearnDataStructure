'''user_input=input()
list=list(map(int,user_input.split(" ")))
x=int(input())'''

























"""base=int(input("enter base: "))
power=int(input("enter power: "))

def pow(base,power):
    if power==0:                        #base case
        return 1
    else:
        out=base*pow(base,power-1)      #recursion
        return out

print(pow(base,power))"""

























"""def findx(list,si,x):
    l=len(list)
    if si==l:
        return -1
    if list[si]==x:
        return si
    smalllist=findx(list,si+1,x) #recursion take place here....
    return smalllist

print(findx(list,0,x))"""






















"""def isSorted(list,si):
    l=len(list)
    if si==l-1 or si==l:
        return True
    if list[si]>list[si+1]:
        return False
    smalllist=isSorted(list,si+1)
    return smalllist"""
































'''def findx(list,x):
    l=len(list)
    if l==0:
        return -1
    if list[0]==x:
        return 1
    b=list[1:]
    smalllist=findx(b,x)  #recursion is taken place here..
    return smalllist

print(findx(list,x))'''
































'''def sumlist(list):
    l=len(list)
    if l==1:
        return list[0]
    b=list[1:]
    smalllist=sumlist(b)  #recursion take place here.
    sum=list[0]+smalllist
    return sum

print(sumlist(list))'''