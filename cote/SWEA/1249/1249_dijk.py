import sys
import heapq

sys.stdin = open("input.txt")
T = int(input())

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(grid, N):
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        cost, x, y = heapq.heappop(heap)

        if cost != dist[x][y]:
            continue

        if x == N - 1 and y == N - 1:
            return cost
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                ncost = cost + grid[nx][ny]
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(heap, (ncost, nx, ny))
    
    return dist[N-1][N-1]




for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    result = dijkstra(grid, N)
    print(f"#{tc} {result}")