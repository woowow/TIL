import sys
#K = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline())

stack = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

total = sum(stack)
print(total)