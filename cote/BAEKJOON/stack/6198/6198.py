import sys

N = int(sys.stdin.readline().rstrip())

#buildings = []
#for _ in range(N):
#    buildings.append(int(sys.stdin.readline().rstrip()))
buildings = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = 0
stack = []

for height in buildings:
    while stack and stack[-1] <= height:
        stack.pop()
    
    cnt += len(stack)
    
    stack.append(height)

print(cnt)



'''
자기보다 높은 건물이 나올때까지 pop

for i, j 이중 반복문을 쓰면 매번 모든 것들을 다 조사해야해서 문제
stack으로 pop을 하면 한 번 버린건 다시 안쓰니까
데이터를 하나 하나 다 확인해야하는 경우에 시간복잡도 손해를 보기때문에, 스택을 활용해서
필요 없는 데이터들은 삭제하면서 쓴다

stack에 append하고, 자기보다 낮으면 pop?
이전 빌딩들 중에 새로 들어온 애의 옥상을 볼 수 있는 애들을 계속해서 +한다
근데 만약 새로 들어온 애보다 높이가 낮으면 어차피 앞으로 아무것도 못 보니 뺀다

'''