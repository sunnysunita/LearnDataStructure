num_disk=int(input("enter number of disk: "))

def tow(num_disk,a,b,c):
    if num_disk==1:
        print(a," ",c)
        return
    tow(num_disk-1,a,c,b)
    print(a," ",c)
    tow(num_disk-1,b,a,c)

tow(num_disk,"a","b","c")