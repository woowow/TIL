'''
미로 탈출

지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기 전에 탈출할 수 있는지 여부, 얼마나 빨리 탈출할 수 있는지

지훈이와 불은 매 분마다 상하좌우로 한칸씩 이동 가능
지훈이는 한칸씩 갈 수 있고, 불은 4 방향으로 확산됨

지훈이는 미로의 가장자리에 접한 공간에서 탈출 가능

R, C 입력 (row, col)
R줄 동안 미로 행
#은 벽, .은 공간, J는 지훈이 초기 위치, F: 불이 난 공간
'''
import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())

map_info = [list(input().rstrip()) for _ in range(R)]

'''

'''

directions = ((1,0), (-1,0), (0,1), (0,-1))

def bfs(map_info):
    jihun = deque()
    fire = deque()

    jihun_time = [[-1] * C for _ in range(R)]
    fire_time = [[-1] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if map_info[i][j] == 'J':
                jihun.append((i,j))
                jihun_time[i][j] = 0
            elif map_info[i][j] == 'F':
                fire.append((i,j))
                fire_time[i][j] = 0

    while fire:
        x, y = fire.popleft()
        for dx, dy in directions:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < R and 0 <= ny < C:
                # 여기서 벽이 아닐 때 퍼져나가게 하니 무한으로 추가가 됐었음
                # 그래서 아직 안와본 곳 (time이 -1인 곳)일 때만 하는 것으로 하니 내가 이미 왔던 곳이 이상해짐
                if map_info[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire.append((nx, ny))

    while jihun:
        x, y = jihun.popleft()
        if x == 0 or x == (R-1) or y == 0 or y == (C-1):
            return 1
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 여기에 추가할건 jihun이가 끝 지점에 도달했을 때
            if nx == 0 or nx == (R-1) or ny == 0 or ny == (C-1):
                if map_info[nx][ny] == '.':
                # 도달했을 때 만약 -1이 아니고 불보다 작거나, 불이 -1이라면 +2해서 출력
                    tmp = jihun_time[x][y] + 1
                    if tmp < fire_time[nx][ny] or fire_time[nx][ny] == -1:
                        return tmp+1

            if 0 <= nx < R and 0 <= ny < C:
                if map_info[nx][ny] == '.' and jihun_time[nx][ny] == -1:
                    tmp = jihun_time[x][y] + 1
                    if tmp < fire_time[nx][ny] or fire_time[nx][ny] == -1:
                        jihun_time[nx][ny] = tmp
                        jihun.append((nx, ny))

    return 'IMPOSSIBLE'

print(bfs(map_info))
