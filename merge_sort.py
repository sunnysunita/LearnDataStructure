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






n=input()
list=list(map(int,n.split()))
mergeSort(list)
for e in list:
    print(e,end=" ")