import sys
input=sys.stdin.readline

def main()->None:
    n=int(input())
    stack=[]
    for _ in range(n):
        op=input().rstrip()
        if op=='pop':
            if len(stack)==0:
                print(-1)
            else:
                print(stack.pop())
        elif op=='size':
            print(len(stack))
        elif op=='empty':
            if len(stack)==0:
                print(1)
            else:
                print(0)
        elif op=='top':
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1]) ##[-1]이 top 역할
        else:
            ops=op.split()
            stack.append(int(ops[1]))

main()