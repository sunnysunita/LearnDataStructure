a=int(input("enter number: "))
b=int(input("enter number: "))
def even(a,b):
    if b==a-1:
        return
    if b%2==0:
        print(b)
    even(a,b-1)




even(a,b)