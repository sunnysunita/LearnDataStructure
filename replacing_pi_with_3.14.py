user_input=input("enter string: ")
list=list(user_input)
print(list)

def rep_pi(list,si):
    l=len(list)
    if si==l:
        return
    if list[si]=="p" and list[si+1]=="i":
        list.pop(si)
        list.pop(si)
        list.insert(si,"3.14")
    return rep_pi(list,si+1)

rep_pi(list,0)

print(list)
str="".join(list)
print(str)