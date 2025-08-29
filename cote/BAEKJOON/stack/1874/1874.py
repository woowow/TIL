import sys

N = int(sys.stdin.readline())

stack = []
cur = 1
result = []
nums = [int(sys.stdin.readline()) for _ in range(N)]

for num in nums:
    while cur <= num:
        stack.append(cur)
        result.append('+')
        cur += 1
    
    if stack[-1] != num:
        print('NO')
        sys.exit()

    stack.pop()
    result.append('-')

for i in result:
    print(i)



'''
cur보다 작은 수는 이미 들어가있으며
만약 순차적으로 pop되는 것이 아닌 더 작은 수가 먼저 pop이 되려면 다음 수은 재 push될 수 없어 불가능해짐
'''