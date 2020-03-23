"""stair=int(input("enter number of steps: "))
def num_ways(stair):
    if stair==0 or stair==1:
        return 1
    if stair==2:
        return 2
    out=num_ways(stair-1)+num_ways(stair-2)+num_ways(stair-3)
    return out

print(num_ways(stair))"""

stair = int(input())


"""def num_ways(stair):
    if stair == 0 or stair == 1:
        return 1
    if stair == 2:
        return 2
    out = num_ways(stair - 1) + num_ways(stair - 2) + num_ways(stair - 3)
    return out"""


def num_ways_BU(stair):
    if stair == 0 or stair == 1:
        return 1
    if stair == 2:
        return 2
    list1 = list(range(0,stair+1))
    list1[0] = 1
    list1[1] = 1
    list1[2] = 2
    for i in range(3,stair + 1):
        list1[i] = list1[i - 1] + list1[i - 2] +list1[i-3]
    return list1[stair]

# print(num_ways(stair))
print(num_ways_BU(stair))