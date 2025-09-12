'''
토마토 보관 창고 M * N

잘 익은 토마토와 잘 익지 않은 토마토 존재

하루가 지나면, 익튼 토마토들의 인접한 곳에 있는 익지 않은 토마토들이 익음

인접 방향은 상 하 좌 우

토마토 정보가 주어졌을 때 모든 토마토가 익는데 걸리는 일수

'''

'''
완탐으로 해당 
'''
from collections import deque

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

days = 0

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(box):
    global days
    stack = deque([])
    
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                stack.append([i, j])

    while stack:
        length = len(stack)
        # 이렇게 할 경우 턴마다 하는게 안돼
        # 턴마다 하려면 하루에 있는 길이만큼 털어야함
        for _ in range(length):
            x, y = stack.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if box[nx][ny] == 0:
                        box[nx][ny] = 1
                        stack.append([nx,ny])
        
        if len(stack) != 0:
            days += 1
    
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1

    return days

bfs(box)

print(days)