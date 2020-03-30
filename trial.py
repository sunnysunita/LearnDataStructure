def intersection(arr1, arr2):
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print(arr1[i])
            i += 1
            j += 1

# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
arr1.sort()
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
arr2.sort()
intersection(arr1, arr2)