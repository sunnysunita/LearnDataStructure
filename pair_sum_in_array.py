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
