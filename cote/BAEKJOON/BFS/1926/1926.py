from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]


# 개수는 어떻게 해야하지?
# 개수는 bfs로 check하면서 visited를 true로 변경, queue가 비면 cnt += 1
# 근데 그럼 그 다음 bfs는 어떻게 하지?
# n이 너무 커지면 터져버리잖아 근데 500x500이면 흠 25000에다가 거기서 bfs를 돌려야하니 너무 커질수도
# bfs로 visited를 true로 돌리고, 최대 cost를 저장하거나, 아님 list에 append해서 마지막에 max?
# 미리 1인 index를 저장해놓자


def bfs(info, x, y):
    queue = deque([])
    extent = 0
    if not visited[x][y]:
        queue.append([x, y])
        visited[x][y] = True

    while queue:
        extent += 1
        x1, y1 = queue.popleft()
        for dx, dy in directions:
            nx, ny = x1+ dx, y1+dy
            if 0 <= nx < N and 0 <= ny < M:
                if info[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    extent_lst.append(extent)
                

extent_lst = []
cnt = 0
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if paper[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs(paper, i, j)

print(cnt)
print(max(extent_lst) if extent_lst else 0)