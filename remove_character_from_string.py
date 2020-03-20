user_input=input("enter string: ")
list=list(user_input)
print(list)
x=input("enter character to remove from string: ")

def rem(list,si,x):
    l=len(list)
    if si==l:
        return
    if list[si]==x:
        list.pop(si)
        return rem(list,si,x)
    else:
        return rem(list,si+1,x)

rem(list,0,x)
print(list)

str="".join(list)
print(str)