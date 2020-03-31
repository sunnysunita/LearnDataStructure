n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
# list.sort()

# print(list)
def sum(list, si, ei):
    out = 0
    for i in range(si, ei + 1):
        out = out + list[i]
    return out


def fun():
    right_sum=sum(list,0,len(list)-1)
    left_sum=0
    for i in range(0, len(list)-1):
        right_sum=right_sum-list[i]
        if i!=0:
            left_sum=left_sum+list[i-1]
        if right_sum==left_sum:
            return i
    return -1
        #if sum(list, 0, i - 1) == sum(list, i + 1, len(list) - 1):
            # print("index=",i," ","value=",list[i])
            #return i
    #return -1

val=fun()
if val == -1:
    print(-1)
else:
    print(val)
