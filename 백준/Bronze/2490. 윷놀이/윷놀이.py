import sys
input=sys.stdin.readline

for _ in range(3):
    s=sum(map(int, input().split()))
    if s==3:
        print("A")
    elif s==2:
        print("B")
    elif s==1:
        print("C")
    elif s==0:
        print("D")
    elif s==4:
        print("E")