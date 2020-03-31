n = int(input())
user_input = input()
list = list(int(i) for i in user_input.strip().split(" "))
d = int(input())
if n >= d:
    list_d = list[0:d]
    list_e = list[d:]
    list = list_e + list_d
# print(list)
else:
    x = d % n
    list_d = list[0:x]
    list_e = list[x:]
    list = list_e + list_d
for e in list:
    print(e, end=" ")
