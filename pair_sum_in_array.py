"""n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
sum = int(input())
list.sort()
print(list)
l = len(list)


def binary_search(list, key, si, ei):
    if si > ei:
        return -1
    mid = (si + ei) // 2
    if list[mid] == key:
        return mid
    elif key < list[mid]:
        return binary_search(list, key, si, mid - 1)
    else:
        return binary_search(list, key, mid + 1, ei)


for e in list:
    req = sum - e
    out = binary_search(list, req, 0, l - 1)  # give index of other element
    if out != -1:
        if e <= list[out]:
            # print(e, " ", list[out])
            while out + 1 <= l and list[out] == req:
                print(e, " ", list[out])
                out += 1

        else:
            # print(list[out], " ", e)
            while out + 1 <= l and list[out] == req:
                print(e, " ", list[out])
                out += 1"""

n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
sum = int(input())
list.sort()
print(list)
l = len(list)
i = 0
j = l - 1
while i < j:
    if list[i] + list[j] > sum:
        j -= 1
    elif list[i] + list[j] < sum:
        i += 1
    else:
        count_i=list.count(list[i])
        count_j=list.count(list[j])
        out=count_i*count_j
        if list[i] < list[j]:
            for e in range(0, out):
                print(list[i], " ", list[j])
        else:
            for e in range(0, out):
                print(list[j], " ", list[e])
        i += count_i
        j -= count_j
