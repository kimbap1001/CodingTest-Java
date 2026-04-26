import sys
from collections import deque
input=sys.stdin.readline

directions=[(1,0), (0,1), (-1,0), (0,-1)]

def bfs(n:int, m:int, board:list[list[int]])->int:
    queue=deque([(0,0)])
    dist=[[0]*m for _ in range(n)]
    dist[0][0]=1
    while queue:
        x,y=queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and dist[nx][ny]==0 and board[nx][ny]==1:
                dist[nx][ny]=dist[x][y]+1
                queue.append((nx,ny))
    return dist[n-1][m-1]

def solve()->int:
    n,m=map(int, input().split())
    board=[list(map(int, list(input().rstrip()))) for _ in range(n)]
    return bfs(n,m,board)

def main()->None:
    print(solve())

main()
