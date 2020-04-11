"""n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
sum = int(input())
list.sort()
#print(list)
l = len(list)
for i in range(0,l):
    for j in range(i+1,l):
        if list[i] + list[j] == sum:
            if list[i]<list[j]:
                print(list[i], list[j])
            else:
                print(list[j], list[i])"""

"""n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
sum = int(input())
list.sort()
list0 = []
print(list)
l = len(list)
for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if list[i]+list[j]+list[k] == sum:
                list0.append(list[i])
                list0.append(list[j])
                list0.append(list[k])
                mini = min(list0)
                print(mini, end=" ")
                list0.remove(mini)
                mini = min(list0)
                print(mini, end=" ")
                list0.remove(mini)
                print(list0[0])
                list0.remove(list0[0])
"""

def findTriplets(arr, n, sum):

    arr.sort()

    for i in range(0, n - 1):

        l = i + 1
        r = n - 1
        x = arr[i]
        while l < r :
            if x + arr[l] + arr[r] == sum :
                list0.append(arr[l])
                list0.append(arr[r])
                list0.append(x)
                mini = min(list0)
                print(mini, end=" ")
                list0.remove(mini)
                mini = min(list0)
                print(mini, end=" ")
                list0.remove(mini)
                print(list0[0])
                list0.remove(list0[0])
                l = l + 1
                r = r - 1

            elif x + arr[l] + arr[r] < sum:
                l = l + 1

            else:
                r = r - 1



num = int(input())
user_input = input()
arr = list(int(i) for i in user_input.strip().split(" "))
sum = int(input())
n = len(arr)
list0 = []

findTriplets(arr, n, sum)