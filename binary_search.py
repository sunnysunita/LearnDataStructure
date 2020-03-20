user_input=input("enter list: ")
list=list(map(int,user_input.split()))
print(list)
key=int(input("enter key element: "))

def binary_search(list,key,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if list[mid]==key:
        return mid
    elif key<list[mid]:
        return binary_search(list,key,si,mid-1)
    else:
        return binary_search(list,key,mid+1,ei)

print(binary_search(list,key,0,len(list)-1))
