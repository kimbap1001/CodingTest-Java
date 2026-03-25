import sys
input=sys.stdin.readline

def solve(nums:list, x:int)->int:
    count=[0]*(x-1)
    result=0

    for num in nums:
        if num<x:
            count[num-1]+=1

    for i,cnt in enumerate(count[:(x-1)//2]):
        if cnt and count[(x-1)-1-i]:
            result+=1
    return result

def main()->None:
    _=input()
    nums=map(int, input().split())
    x=int(input())
    print(solve(nums, x))

main()