a=int(input("enter number, a= "))
b=int(input("enter number, b= "))

def multi_a_and_b(a,b):
    if b==0 or a==0:
        return 0
    if b==1:
        return a
    out=a+multi_a_and_b(a,b-1)
    return out
print(multi_a_and_b(a,b))