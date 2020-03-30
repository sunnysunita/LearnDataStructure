user_input=input("enter value of x and y")
list=list(map(int,user_input.split(" ")))
x=list[0]
y=list[1]
print(x,y)
def power(x,y):
    if y==0:
        return 0
    elif y==1:
        return x
    else:
        small_power=power(x,y//2)
        if y%2==0:
            return small_power*small_power                                     #power(x,y//2)*power(x,y//2)
        else:
            return x*small_power*small_power                                     #x*power(x,y//2)*power(x,y//2)

print(power(x,y))
