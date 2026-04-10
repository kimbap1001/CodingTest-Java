import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
nums=deque([i+1 for i in range(n)])
for _ in range(n-1):
    nums.popleft()
    nums.append(nums.popleft())
print(nums[0])