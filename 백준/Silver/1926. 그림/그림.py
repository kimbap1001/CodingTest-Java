import sys
from collections import deque
input=sys.stdin.readline

directions=[(1,0), (0,1), (-1,0), (0,-1)]

def bfs(n:int, m:int, board:list[list[int]], visited:list[list[bool]], start:tuple[int, int])->int:
    queue=deque([start])
    visited[start[0]][start[1]]=True
    size=1

    while queue:
        x, y=queue.popleft()
        for dx, dy in directions:
            nx, ny=x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))
                size+=1
    return size

def solve(n:int, m:int, board:list[list[int]])->list[int]:
    visited=[[False]*m for _ in range(n)]
    paints=[]

    for nx in range(n):
        for ny in range(m):
            if not visited[nx][ny] and board[nx][ny]:
                paints.append(bfs(n,m,board,visited,(nx,ny)))

    return paints

def main()->None:
    n,m=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    ans=solve(n,m,board)
    print(len(ans))
    print(max(ans) if ans else 0)

main()