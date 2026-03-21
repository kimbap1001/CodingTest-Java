import sys
input=sys.stdin.readline

def solve()->None:
    nums=[int(input()) for _ in range(5)]
    nums.sort()
    print(int(sum(nums)/5))
    print(nums[2])

if __name__=="__main__":
    solve()