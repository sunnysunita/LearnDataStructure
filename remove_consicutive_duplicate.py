user_input=input("enter string: ")
list=list(user_input)
print(list)

def rem_dup(list,si):
    l=len(list)
    if si==l:
        return
    x=list[si]
    while si+1<l and list[si+1]==x:
        list.pop(si+1)
        l-=1
    return rem_dup(list,si+1)

rem_dup(list,0)
print("".join(list))
