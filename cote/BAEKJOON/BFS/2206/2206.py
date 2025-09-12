'''
벽 부수고 이동하기

NxM의 행렬로 표현되는 맵

0은 이동할 수 있는 곳
1은 이동할 수 없는 벽

(1,1)에서 (N,M)의 위치까지 이동하려는데, 최단 경로로 이동하려 함
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로
시작 칸과 끝 칸도 포함해서 셈

이동하는 도중, 한 개의 벽을 부수고 이동하는게 경로가 더 짧다면, 한 개 부수고 이동해도 됨

최단 경로를 구해내는 프로그램
'''

'''
어떻게 해야하지
bfs로 넣는건 동일한데
어떤 1을 부셔야 최단일지를 찾아야함

0과 0 사이를 1이 막는 케이스에 대해서만 고려해서 부신다?
'''
from collections import deque

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

N, M = map(int, input().split())

map_info = [list(map(int, input())) for _ in range(N)]

# break_wall = []

# for i in range(N):
#     for j in range(M):
#         # 부수면 건너편이 0인 지점들을 찾아서 그 지점들에 대해 모두 bfs
#         if map_info[i][j] == 1:
#             for dx, dy in directions:
#                 ny = i + dy
#                 nx = j + dx
#                 px = j - dx
#                 py = i - dy
#                 if 0 <= nx < M and 0 <= ny < N:
#                     if 0 <= px < M and 0 <= py < N:
#                         if map_info[py][px] == 0 and map_info[ny][nx] == 0:
#                             break_wall.append((i, j))

# break_wall = list(set(break_wall))

# def bfs(info):
#     global dist
#     q = deque([(0, 0)])
    
#     while q:
#         x, y = q.popleft()

#         if info[y][x] > dist:
#             break

#         if x == (M-1) and y == (N-1):
#             return info[y][x]

#         for dx, dy in directions:
#             nx = x + dx
#             ny = y + dy

#             if 0 <= nx < M and 0 <= ny < N:
#                 if info[ny][nx] == 0:
#                      info[ny][nx] = info[y][x] + 1
#                      q.append((nx, ny))
    
#     return 1000000

# dist = 1000000
# for x, y in break_wall:
#     info = [row[:] for row in map_info]
#     info[x][y] = 0
#     info[0][0] = 1
#     dist = min(dist, bfs(info))

# if dist == 1000000:
#     dist = -1
# print(dist)


# # 시간 초과가 남 모든 부술 수 있는 벽에 대해서 bfs를 다 따져서 그런듯

dist = [[[0]*2 for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 1

def bfs():
    q = deque([(0, 0, 0)])

    while q:
        x, y, chk = q.popleft()
        
        if x == (M-1) and y == (N-1):
            return dist[y][x][chk]
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if map_info[ny][nx] == 0 and dist[ny][nx][chk] == 0:
                    dist[ny][nx][chk] = dist[y][x][chk] + 1
                    q.append((nx, ny, chk))
                
                elif map_info[ny][nx] == 1 and chk == 0 and dist[ny][nx][1] == 0:
                    dist[ny][nx][1] = dist[y][x][chk] + 1
                    q.append((nx, ny, 1))
    
    return -1


print(bfs())
