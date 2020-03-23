user_input=input("enter string: ")
list0=list(user_input)
print(list0)

def pair_star(list0,si):
    l=len(list0)
    if si==l or si==l-1:
        return
    x=list0[si]
    if list0[si+1]==x:
        list0.insert(si+1,"*")
        return pair_star(list0,si+2)
    else:
        return pair_star(list0,si+1)

pair_star(list0,0)
#print(list0)
print("".join(list0))