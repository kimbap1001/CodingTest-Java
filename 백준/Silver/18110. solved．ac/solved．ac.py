import math
def myround(x):
    x1=math.floor(x)
    if x<x1+0.5:
        return x1
    else:
        return x1+1

n=int(input())
if n==0:
    print(0)
    exit(0)
cut=myround(n*0.15)
get=n-2*cut
level=list()
sum=0
for i in range(n):
    level.append(int(input()))
level.sort()
Rlevel=level[cut:n-cut]
for i in range(get):
    sum+=Rlevel[i]
avg=myround(sum/get)
print(avg)