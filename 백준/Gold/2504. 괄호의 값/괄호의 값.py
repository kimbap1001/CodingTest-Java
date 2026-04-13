import sys
input=sys.stdin.readline

def check(word:str)->bool:
    stack=[]
    for alpha in word:
        if alpha==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
        elif alpha==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                return False
        else:
            stack.append(alpha)
    if stack:
        return False
    else:
        return True

def solve(word:str)->int:
    if not check(word):
        return 0
    
    stack1=[]
    stack2=[]
    stack3=[]
    result=0
    
    #1. '()', '[]' 계산
    for alpha in word: 
        if stack1 and stack1[-1]=='(' and alpha==')':
            stack1.pop()
            stack1.append(2)
        elif stack1 and stack1[-1]=='[' and alpha==']':
            stack1.pop()
            stack1.append(3)
        else:
            stack1.append(alpha)
    
    #2. '(x)', '[x]' 계산
    for i, alpha in enumerate(stack1):
        if alpha==')' and stack1[i-2]=='(':
            stack2.pop()
            stack2.pop()
            stack2.append(2*stack1[i-1])
        elif alpha==']' and stack1[i-2]=='[':
            stack2.pop()
            stack2.pop()
            stack2.append(3*stack1[i-1])
        else:
            stack2.append(alpha)

    #3. '(xy)', '[xy]' 계산
    for alpha in stack2:
        sum1=0
        if alpha==')':
            while isinstance(stack3[-1], int):
                sum1+=stack3.pop()
            stack3.pop()
            stack3.append(2*sum1)
        elif alpha==']':
            while isinstance(stack3[-1], int):
                sum1+=stack3.pop()
            stack3.pop()
            stack3.append(3*sum1)
        else:
            stack3.append(alpha)

    
    
    #print(*stack1)
    #print(*stack2)
    #print(stack3)
    
    return sum(stack3)


def main()->None:
    print(solve(input().rstrip()))


main()