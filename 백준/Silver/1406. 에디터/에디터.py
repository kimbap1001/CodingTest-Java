import sys
input=sys.stdin.readline

def solve(origin:str, n:int)->None:
    result_front=list(origin) ##커서 앞
    result_back=[]  ##커서 뒤
    for _ in range(n):
        opcode=input().rstrip()
        if opcode=='L' :
            if len(result_front) != 0:
                result_back.append(result_front.pop()) ##커서 앞에서 pop해서 커서 뒤에 push
        elif opcode=='D' : 
            if len(result_back) != 0:
                result_front.append(result_back.pop()) ##커서 뒤에서 pop해서 커서 앞에 push
        elif opcode=='B' :
            if len(result_front) != 0:
                result_front.pop()
        else:
            result_front.append(opcode[2])
    result_back.reverse()
    print("".join(result_front)+"".join(result_back))

def main()->None:
    origin=input().rstrip()
    n=int(input())
    solve(origin, n)


main()