user_input=input("enter list: ")
input_list=list(map(int,user_input.split()))
#print(input_list)

def isSorted(input_list):
    l=len(input_list)
    if l==0 or l==1:
        return True
    if input_list[0]>input_list[1]:
        return False
    b=input_list[1:]
    isSmallerListSorted=isSorted(b)
    return isSmallerListSorted

print(isSorted(input_list))