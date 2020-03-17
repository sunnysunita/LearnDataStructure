num=int(input("enter number: "))

def fib(num):
    if num==1 or num==2:
        return 1
    output=fib(num-1)+fib(num-2)
    return output

print(fib(num))