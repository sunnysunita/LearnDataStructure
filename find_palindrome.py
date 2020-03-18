num=int(input("enter number:"))

def pal(num,t):   #t=0
    if num==0:
        return t
    else:
        t=(t*10)+num%10
        return pal(int(num/10),t)

if num==pal(num,0):
    print("Palindrome number.")
else:
    print("Not Palindrome number.")
