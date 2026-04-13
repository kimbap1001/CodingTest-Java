import sys
input=sys.stdin.readline

def solve(word:str)->None:
    stack=[]
    for alpha in word:
        if alpha=='(':
            stack.append(alpha)
        else:
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                print('NO')
                return
    
    if stack:
        print('NO')
    else:
        print('YES')


def main()->None:
    for _ in range(int(input())):
        solve(input().rstrip())


main()