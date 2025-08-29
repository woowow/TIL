import sys

left = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
right = []
#cursor = len(string) - 1

for _ in range(M):
    op = sys.stdin.readline().rstrip()
    
    if op[0] == 'L':
        if left:
            right.append(left.pop())
    
    elif op[0] == 'D':
        if right:
            left.append(right.pop())
    
    elif op[0] == 'B':
        if left:
            left.pop()
    
    elif op[0] == 'P':
        left.append(op[2])

print("".join(left + right[::-1]))

'''
시간 제한이 짧다
고로, stack을 두개 둬서 커서 위치를 둔다
커서 기준 왼쪽에 있는 애들을 left 배열에
오른쪽에 있는 애들을 right 배열에

만약 B라면 어차피 커서 왼쪽에 있는걸 없애기때문에 left.pop
P라면 커서 왼쪽에 삽입하기때문에 left.append
L과 D는 커서를 옮긴다는 것, 즉 left와 right의 구성값을 섞어줘야함
'''