user_input=input("enter string: ")
list=list(user_input)
print(list)

def rep_a_with_b(list,si):
    l=len(list)
    if si==l:
        return
    if list[si]=="a":
        list[si]="b"
    return rep_a_with_b(list,si+1)


rep_a_with_b(list,0)
print(list)