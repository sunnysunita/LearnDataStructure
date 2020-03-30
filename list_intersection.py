m=int(input())
user_input=input()
list_m=list(int(i) for i in user_input.strip().split(" "))

n=int(input())
user_input=input()
list_n=list(int(i) for i in user_input.strip().split(" "))

def merge(smalllist1,smalllist2,list):
    i=0
    j=0
    k=0
    while i<len(smalllist1) and j<len(smalllist2):
        if smalllist1[i]<smalllist2[j]:
            list[k]=smalllist1[i]
            i+=1
            k+=1
        else:
            list[k]=smalllist2[j]
            j+=1
            k+=1
    while i<len(smalllist1):
        list[k]=smalllist1[i]
        i+=1
        k+=1
    while j<len(smalllist2):
        list[k]=smalllist2[j]
        j+=1
        k+=1


def mergeSort(list):
    if len(list)==1 or len(list)==0:
        return
    mid=len(list)//2

    smalllist1=list[0:mid]
    smalllist2=list[mid:]
    mergeSort(smalllist1)               #T(n/2)
    mergeSort(smalllist2)               #T(n/2)

    merge(smalllist1,smalllist2,list)   #O(n)



mergeSort(list_m)
mergeSort(list_n)






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






#list_m.sort()
#list_n.sort()
#list=[]

for e in list_m:
    if binary_search(list_n, e, 0, len(list_n) - 1) != -1:
        print(e)
        #list.append(e)
        list_n.remove(e)