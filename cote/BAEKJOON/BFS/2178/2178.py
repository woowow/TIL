from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(labyrinth, queue, visited, N, M):
    
    while queue:
        x, y, cost = queue.popleft()
        
        row = N - 1
        col = M - 1
        if x == row and y == col:
            return cost

        for dx, dy in directions:
            if 0 <= x + dx < N and 0 <= y + dy < M:
                if labyrinth[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                    queue.append([x+dx, y+dy, cost+1])
                    visited[x+dx][y+dy] = True
    



if __name__ == '__main__':
    N, M = map(int, input().split())

    labyrinth = [list(map(int, input().strip())) for _ in range(N)]
    start = 0
    queue = []
    queue = deque(queue)
    queue.append([0, 0, 1])
    visited = [[False] * M for _ in range(N)] 
    visited[0][0] = True
    result = bfs(labyrinth, queue, visited, N, M)

    print(result)


# BFS는 너비 우선 탐색
# 시작지점을 queue에 넣고 queue에서 하나씩 pop하면서 해당 위치에서 갈 수 있는 다음 위치를 계속해서 queue에 넣음
# visited와 함께 설정해서 이미 갔던 곳은 방문 ㄴㄴ
# 그렇게 해서 원하는 지점에 도달하면 끝
# 근데 최소 칸 수를 출력해야해 그건 어떻게 하지? 
# 해당 칸에 대해 cost를 계속 연결해놔야할듯
# 좌표랑 cost 묶어놔야겠네