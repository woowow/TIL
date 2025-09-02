import sys
from collections import deque

sys.stdin = open("input.txt")

T = int(input())

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(labyrinth, N):
    queue = deque()
    queue.append((0, 0))
    
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            cost = visited[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                cost += labyrinth[nx][ny]
                if cost < visited[nx][ny]:
                    visited[nx][ny] = cost
                    queue.append((nx, ny))
    
    return visited[N-1][N-1]
    

for tc in range(1, T+1):
    N = int(input())
    labyrinth = [list(map(int, input().strip())) for _ in range(N)]

    result = bfs(labyrinth, N)

    print(f"#{tc} {result}")