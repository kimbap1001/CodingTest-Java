import sys
input=sys.stdin.readline

def solve()->None:
    nums=map(int,input().split())
    index=[0 for _ in range(6)]
    for num in nums:
        index[num-1]+=1
    for i in range(len(index)):
        if index[i]==3:
            print(10000+1000*(i+1))
            return
    for i in range(len(index)):
        if index[i]==2:
            print(1000+100*(i+1))
            return
    for i in range(len(index)-1,-1,-1):
        if index[i]==1:
            print(100*(i+1))
            return

if __name__=="__main__":
    solve()    