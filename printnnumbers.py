num=int(input("enter number: "))
def print_1_to_n(num):
    if num==0:
        return
    print_1_to_n(num-1)
    print(num)

print_1_to_n(num)


"""num=int(input("enter number: "))

def printn(num):
    if num==0:
        exit()
    print(num)
    printn(num-1)

printn(num)"""