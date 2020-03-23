user_input=input("enter string: ")
list = list(user_input)
print(list)

def conv_str_to_int(list,si,l=len(list)):
    if si==l:
        return
    list[si]=int(list[si])
    return conv_str_to_int(list,si+1,l)

conv_str_to_int(list,0)
for e in list:
    print(e,end="")