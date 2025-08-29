N = int(input())

lst = list(map(int, input().split()))

X = int(input())

left, right = 0, N-1
cnt = 0

lst.sort()

while left < right:
    s = lst[left] + lst[right]
    if s == X:
        cnt += 1
        left += 1
        right -= 1
    elif s < X:
        left += 1
    else:
        right -= 1
        

print(cnt)