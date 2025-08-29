import sys

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().split()))

# # 내가 짠 코드
# stack = []
# result = []

# for i in range(N):
#     while stack and stack[-1][1] < A[i]:
#         result.append([stack[-1][0], A[i]])
#         stack.pop()

#     stack.append([i, A[i]])

# for idx, val in stack:
#     result.append([idx, -1])

# result.sort(key=lambda x: x[0])

# for idx, target in result:
#     print(target, end=' ')


# GPT
# 나는 result에 idx, val을 다 넣고 idx별로 sorting을 걸어버리고 그 중 val만 출력하게 했다
# 근데 그냥 result에 저장할 때 idx에 맞는 위치에 val을 추가하면 된다
# 왜? result의 전체 길이를 나는 알고 있으니까
# 그리고 초기화할 때 -1로 걸어버리면 스택에 남은 애들에 대해선 굳이 -1로 지정해주는 과정을 생략해도 된다

stack = []
result = [-1] * N

for i in range(N):
    while stack and stack[-1][1] < A[i]:
        idx, val = stack.pop()
        result[idx] = A[i]
    stack.append([i, A[i]])

print(*result)


'''
이것도 마찬가지로 검사하고 stack에 넣기?
만약, 새로 받은 숫자가 stack의 top보다 크면?
stack의 top은 오큰수 계산에 필요가 없으니 pop

stack에 새로운 애를 쌓고
만약 stack top에 있는 애보다 새로 들어온 수가 크면
걔는 result에 지금 새로 들어온 수의 index를 추가해주고 pop해버려야지
근데 새로 들어온 수가 stack top에 있는 애보다 작아?
그럼 pop을 하면 안돼

result에 index를 추가하기 위해선 지금 애가 몇번째 index인지 알아야해

고로 stack에 [index, val] 이런 식으로 저장을 해야한다

stack에 그렇게 저장하고 마지막에 index순으로 sorted 갈겨서 출력하면 될듯
'''