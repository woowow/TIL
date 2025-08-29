import sys

N = int(sys.stdin.readline().rstrip())

tower = list(map(int, input().split()))

# # 시간 초과
# result = [0]

# for i in range(1, len(tower)):
#     chk = False
#     for j in range(i-1, 0, -1):
#         if tower[i] < tower[j]:
#             chk = True
#             result.append(j+1)
#             break
#     if chk == False:
#         result.append(0)

# print(*result, end=' ')

stack = []
result = []
for i in range(N):
    height = tower[i]
    
    while stack and stack[-1][1] < height:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0])
    
    stack.append([i+1, height])

print(*result)
    
'''
반드시 왼쪽만을 바라봐야함
본인보다 높은 값 중 가장 가까운 타워를 찾아야함

근데 탑의 수는 50만이며, 높이는 1억임
ㅋ
ㅋ
n(n+1)/2
O(n^2) => 250000000000 터짐

가장 단순한 알고리즘
각 타워별로 본인 idx부터 왼쪽으로 하나씩 깎아가며 가장 가까운 자기보다 높은 값 찾기

index를 찾으면 O(n^2)
'''