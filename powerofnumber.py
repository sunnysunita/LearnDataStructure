xandy = input("inputs: ")
list = list(map(int, xandy.split()))
x = list[0]
y = list[1]

def pnum(x,y):
    if y==0:
        return 1
    output=x*pnum(x,y-1)
    return output

print(pnum(x,y))