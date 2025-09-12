'''
건물은 F층으로 이루어짐

그 중, 스타트링크은 G 층에 속함

강호는 S층에 존재하며 G층으로 이동하고자 함

시작 지점 : S, 최대 길이 F, 목표 : G

버튼은 2개로 U 버튼과 D 버튼만 존재

U버튼은 누르면 무조건 U개만큼 위로, D버튼은 누르면 D개만큼 아래로 가짐

버튼을 최소 몇 번 눌러야하는지, G층에 갈 수 없으면 "use the stairs" 출력

F, S, G, U, D가 주어짐

1 <= S, G <= F <= 1000000, 0 <= U, D <= 1000000
'''

from collections import deque

F, S, G, U, D = map(int, input().split())

move = [-1] * (F+1)
move[S] = 0
def bfs():

    q = deque([S])
    
    while q:
        height = q.popleft()

        if height == G:
            return move[height]
        
        for nh in (height+U, height-D):
            if nh <= F and 1 <= nh and move[nh] == -1:
                move[nh] = move[height] + 1
                q.append(nh)
    
    return "use the stairs"

print(bfs())