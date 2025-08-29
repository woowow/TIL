import sys

N = int(sys.stdin.readline())

height = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
cnt = 0

for i in range(N):
    same = 1
    while stack and stack[-1][0] < height[i]:
        cnt += stack[-1][1]
        stack.pop()

    if stack and stack[-1][0] == height[i]:
        cnt += stack[-1][1]
        same = stack[-1][1] + 1
        stack.pop()
        if stack:
            cnt += 1
    
    elif stack:
        cnt += 1
            
    stack.append([height[i], same])

print(cnt)

'''
각 사람마다 끝까지 가면서, 서로 볼 수 있는 쌍을 구해야함
즉, 볼 수 있는 쌍이 나올 때마다 cnt를 증가시키면 돼

stack top보다 큰 수가 들어온다
pop해야함, 걔는 이제 더 이상 마주볼 수 없으니까

'''