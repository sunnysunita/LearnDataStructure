num=int(input("enter numbr: "))
def isPrime(num,i):
    if i==1:                          #base case...
        return True
    if num%i==0:
        return False
    return isPrime(num,i-1)           #recurision...

print(isPrime(num,int(num/2)))