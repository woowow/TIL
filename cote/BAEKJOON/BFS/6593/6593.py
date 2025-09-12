'''
빌딩에 갇혀서 탈출하는 가장 빠른 길을 찾아야한다

빌딩은 각 변의 길이가 1인 정육면체로 이루어져있음

이동할 수 있거나, 없거나로 구성

1분마다 각 칸에서 동서남북상하로 1칸씩 이동할 수 있음

출구로만 나갈 수 있음

입력은 여러 개의 테스트 케이스로 이루어지며(while문), L, R, C로 시작

L은 1 <= L <= 30, 층 수, 높이
R은 1 <= R <= 30, 한 층의 행, 세로
C는 1 <= C <= 30, 한 층의 열, 가로

#은 지나갈 수 없는 칸
.은 지나갈 수 있는 칸
S는 시작 지점
E는 출구
'''

from collections import deque

directions = ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1))


def bfs(building, S, L, R, C):
    q = deque([S])
    building_map = [[[-1]*C for _ in range(R)] for _ in range(L)]
    z, y, x = S
    building_map[z][y][x] = 0

    while q:
        z, y, x = q.popleft()

        if building[z][y][x] == 'E':
            return f'Escaped in {str(building_map[z][y][x])} minute(s).'
        
        for dz, dy, dx in directions:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                if building[nz][ny][nx] == '.' or building[nz][ny][nx] == 'E':
                    if building_map[nz][ny][nx] == -1:
                        building_map[nz][ny][nx] = building_map[z][y][x] + 1
                        q.append((nz, ny, nx))
        
    return 'Trapped!'
        

while True:
    
    building = []
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    floor = []
    for i in range(L):
        for j in range(R):
            row = list(input().rstrip())
            for k in range(len(row)):
                if row[k] == 'S':
                    S = (i, j, k)
                elif row[k] == 'E':
                    E = (i, j, k)
            floor.append(row)
        building.append(floor)
        floor = []
        input()

    '''
    탈출이 가능 S에서 시작해서 .을 확인하는데 그걸 i, j, k로 확인해야하나봄

    z가 맨 앞, y가 두번째, x가 세번째
    '''


    print(bfs(building, S, L, R, C))