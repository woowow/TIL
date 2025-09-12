'''
문제

프로젝트를 수행해야함
프로젝트 팀원 수에 제한은 없음

모든 학생들이 한 팀인 경우도 있음

팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 함

혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능함

학생들은 s1, s2 .. , sr

선택하면 그 사람이랑 무조건 팀이다
근데, 만약 혼자 하기로 선택했으면 그 사람은 배제다
이게 가장 최우선이다

어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산

테스트 케이스 개수 T가 주어짐
첫 줄에는 학생의 수 n이 주어짐
둘째 줄에는 선택한 번호가 나옴
'''

'''
풀이 방식
서로소 집합?
일단 혼자 팀하고 싶은 애를 먼저 배제시키고, 나머지를 서로소 집합과 union으로 묶음
단, 묶는 과정에서 혼자 집합하고 싶은 애가 있으면 그 케이스는 바로 배제

시간 초과가 나버림

'''
T = int(input())

# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]

# def union(a, b):
#     pa = find_parent(a)
#     pb = find_parent(b)

#     if pa < pb:
#         parent[pb] = pa
#     else:
#         parent[pa] = pb

# for _ in range(T):
#     n = int(input())
#     choice = list(map(int, input().split()))
#     choice.insert(0, 0)
#     alone = set()

#     for i in range(1, n+1):
#         if i == choice[i]:
#             alone.add(i)

#     parent = [i for i in range(n+1)]

#     for i in range(1, n+1):
#         if find_parent(choice[i]) in alone:
#             parent[i] = find_parent(choice[i])

#         else:
#             a = choice[i]
#             b = i
#             union(a, b)

#     cnt = 0
#     for i in range(1, n+1):
#         if find_parent(i) in alone:
#             if i != find_parent(i):
#                 cnt += 1
#     print(cnt)

'''
시간 제한이 3초, 즉 3억까지 허용

10만개니까 n^2 가면 100억 절대 안돼

nm으로 m이 1000까지 가능, 또는 3000

그럼 n에서 탐구하는 식으로 해야할듯

queue에 한번씩만 넣는다라.. 그럼 dfs네
dfs로 연결해서 자료구조에 추가한다?


'''
import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result
    visited[x] = True
    stack.append(x)

    next = choice[x]
    if not visited[next]:
        dfs(next)
    elif not finished[next]:
        cycle = stack[stack.index(next):]
        result += len(cycle)
    
    finished[x] = True
    stack.pop()



for _ in range(T):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    finished = [False] * (n+1)
    result = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            stack = []
            dfs(i)

    print(n - result)

    # dfs를 돌려서 집합을 구성하고 만약 해당 집합에 alone이 있다면? 전부 cnt에 추가
    # 그리고 cnt에서 alone 개수만큼 빼면 끝

    # 구성되는게 더 이상 뻗어나갈 곳이 없다 즉, 서로가 서로를 가리키고 있다

    # 근데 2중 배열은 해야함
    # cnt로 해서 그게 몇 번째 집합인지 보고 뒤늦게 거길 가리키는 애가 있으면 추가해야하니까

    # 기준을 만족하면 return을 해야 dfs같은 재귀방식이 멈춤
    # 그걸 visited로 하기
    
    # 반복문에 대해 bfs를 돌리더라도 어차피 그 반복문에서 만약 visited가 true면 bfs를 수행 안할거니까 결과적으로 n일듯?

    # dfs는 O(2N)이 나올것이며, 그 집합 안에서 alone이 있는지 확인하는 것도 O(N)으로 O(3N)이 나올듯


'''
기존에 했던 방식은 문제 이해를 잘못했음

이해했던 방식 : 혼자 조를 하고싶은 사람을 고르지만 않으면 팀을 구성할 수 있다
=> 일단 조를 다 짜보고, 그 조 안에 혼자 조를 하고 싶은 사람이 존재하면 그 사람 제외 나머지의 숫자를 다 더하자

문제 방식 : 반드시 싸이클이 구성이 되어야 조를 이룸, 1->3, 3->1, 2->1 이면 1과 3만 같은 조, 2는 아님

'''