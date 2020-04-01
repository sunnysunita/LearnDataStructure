"""n=int(input())
user_input=input()
list=list(int(i) for i in user_input.strip().split(" "))
list.sort()
print(list)
uniq=[]
for e in list:
    if e not in list[list.index(e)+1:]:
        uniq.append(e)
        list.remove(e)
for e in uniq:
    print(e,end=" ")"""

"""list=[1, 2, 2, 3, 3, 6, 6]
tup_list=tuple(list)
set_list=set(list)
for e in set_list:
    #print(e," occurrence=",tup_list.count(e))
    if tup_list.count(e)==1:
        print(e)"""

"""n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
list.sort()
print(list)
uni = []
# for i in range(0,len(list)):
l=len(list)
i=0
while i < l:
    # if i+1==len(list):
    #     uni.append(list[i])
    if i+1 < l and list[i + 1] > list[i]:
        uni.append(list[i])
    else:
        if i+1<l:
            i=i+1
        # if i+1<len(list):
        #     for j in range(i + 1, len(list)):
        #         if list[j] > list[i]:
        #             i = j - 1
    i += 1

print(uni)"""

n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))

out = 0
for e in list:
    out = out ^ e

print(out)