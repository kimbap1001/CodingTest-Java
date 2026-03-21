n=int(input())
stk=[i+1 for i in range(n)]
pp=list()
prev=int(input())
index=prev-1
ispos=True
for i in range(prev):
    pp.append("+")
pp.append("-")
for i in range(n-1):
    num=int(input())
    if num<prev:
        if (index==0)or(num<stk[index-1]):
            ispos=False
            break
        else:
            index=index-1
    else:
        for i in range(stk.index(num)-index):
            pp.append("+")
            index=index+1
        index=index-1
    del stk[stk.index(prev)]
    pp.append("-")
    prev=num
if ispos:
    for i in range(len(pp)):
        print(pp[i])
else:
    print("NO")