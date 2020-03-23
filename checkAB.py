user_input=input("enter string")
list0=list(user_input)

def checkAB(list0,si):
    l=len(list0)
    if si==l:
        return True
    if list0[si]=="a":
        si+=1
        return checkAB(list0,si)
    if list0[si]=="b" and list0[si+1]="b":
            si=si+2


print(checkAB(list0,0))