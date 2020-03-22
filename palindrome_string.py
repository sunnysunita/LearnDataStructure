



user_input=input("enter string: ")
list=list(user_input)
print(list)

def pal(list):
    l=len(list)
    if l==1 or l==0:
        return 1
    if list[0]!=list[l-1]:
        return -1
    b=list[1:l-1]
    return pal(b)

print(pal(list))


"""def pal(list):
    l=len(list)
    i=0
    j=l-1
    while i < j or i != j:
        if list[i]==list[j]:
            i+=1
            j-=1
        else:
            return -1
    return 1

print(pal(list))
"""