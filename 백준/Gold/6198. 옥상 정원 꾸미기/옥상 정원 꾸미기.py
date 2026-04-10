import sys
input=sys.stdin.readline

def solve(towers:list)->int:
    towers.reverse() #구현 편의를 위해 역순처리
    stack=[(1000000001,0)] 
    result=0
    for tower in towers:
        while tower[0]>stack[-1][0]:
            stack.pop()
        result += tower[1] - stack[-1][1] - 1 #스택 탑과 현재 빌딩의 위치 사이의 빌딩 개수를 추가
        stack.append(tower)
    return result


def main()->None:
    n=int(input())
    #단조 감소 스택을 활용하기 위해 빌딩 위치는 역순으로 저장
    towers=[(val, n-i) for i, val in enumerate([int(input()) for _ in range(n)])]
    print(solve(towers))

main()