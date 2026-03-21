import sys
input=sys.stdin.readline

def solve()->None:
    a,b=map(int, input().split())
    if a>b:
        print(a-b-1)
        list=[i for i in range(b+1, a)]
        print(*list)
    elif a==b:
        print(0)
    else:
        print(b-a-1)
        list=[i for i in range(a+1, b)]
        print(*list)

if __name__=="__main__":
    solve()