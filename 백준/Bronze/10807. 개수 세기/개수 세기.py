_=input()
nums=map(int, input().split())
find=int(input())
sum=0
for num in nums:
    if num==find:
        sum+=1
print(sum)