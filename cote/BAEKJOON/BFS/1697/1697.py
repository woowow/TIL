'''
숨바꼭질

수빈이는 점 N에 있고 동생은 점 K에 있음

수빈이는 걷거나 순간이동이 가능

수빈이가 X에 있다면 1초 후에, X-1 또는 X+1로 이동 가능, 순간이동한다면 1초 후에 X * 2로 이동 가능

수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하시오

'''
from collections import deque

N, K = map(int, input().split())

# while True:
#     if abs(K-x) >= x/2:
#         x = x * 2
#         cnt += 1
#     else:
#         if x > K:
#             x = x-1
#             cnt += 1
#         else:
#             x = x+1
#             cnt += 1
#     print(cnt, x)
#     if x == K:
#         print(cnt)
#         break

# '''
# 이 방식은 최적해를 구할 수 없음
# '''

dist = [-1]*100001
dist[N] = 0

def bfs():
    q = deque([N])

    while q:
        x = q.popleft()

        if x == K:
            print(dist[x])
            break
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()

'''
가중치가 동일할 때 최단 거리를 찾는 표준 방법 = BFS
'''