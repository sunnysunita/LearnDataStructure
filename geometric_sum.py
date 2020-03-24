import math
k=int(input("enter value of k: "))

def geo_sum(k):
    if k==0:
        return 1
    else:
        out=geo_sum(k-1)+(1/math.pow(2,k))
        return out
#print(geo_sum(k))
print('%.5f'%geo_sum(k))
