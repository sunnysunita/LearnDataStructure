user_input=input("enter string: ")
list=list(user_input)
x=input("enter character to replace: ")
y=input("enter replacing character: ")
print(list)

def rep_x_with_y(list,si,x,y):
    l=len(list)
    if si==l:
        return
    if list[si]==x:
        list[si]=y
    return rep_x_with_y(list,si+1,x,y)


rep_x_with_y(list,0,x,y)
print(list)
str1=""
str1=str1.join(list)
print(str1)