import sys
input=sys.stdin.readline
from collections import deque
import json

def solve(nums:deque, funcs:str)->None:
    is_Reversed=False
    for func in funcs:
        if func=='R':
            is_Reversed=not is_Reversed
        elif len(nums)==0:
            print('error')
            return
        elif is_Reversed:
            nums.pop()
        else:
            nums.popleft()
    if is_Reversed:
        nums.reverse()
    print('['+','.join(map(str,nums))+']')

def main()->None:
    n=int(input())
    for _ in range(n):
        funcs=input().rstrip()
        _=input()
        nums_raw=input().rstrip()
        # json.loads는 '[]'를 []로, '[1,2,3]'을 [1, 2, 3]으로 바로 바꿔준다.
        nums=deque(json.loads(nums_raw))
        solve(nums, funcs)

main()