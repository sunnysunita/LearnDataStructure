num=int(input("enter number: "))
def sum_of_num(num):
    if num == 0:
        return 0
    sum = num+sum_of_num(num-1)
    return sum

print(sum_of_num(num))
