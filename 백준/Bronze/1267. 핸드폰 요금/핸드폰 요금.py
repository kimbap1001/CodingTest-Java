import sys
input=sys.stdin.readline

def solve()->None:
    m,n=(0,0)
    _=input()
    calls=map(int,input().split())
    for call in calls:
        m+=10*int(call/30)+10
        n+=15*int(call/60)+15
    if m<n:
        print("Y "+str(m))
    elif(m==n):
        print("Y M "+str(n))
    else:
        print("M "+str(n))


if __name__=="__main__":
    solve()
