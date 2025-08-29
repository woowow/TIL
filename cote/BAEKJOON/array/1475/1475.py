N = input()

lst = [0] * 10
cnt = 0

for num in '0123456789':
    nums = N.count(num)
    lst[cnt] = nums
    cnt += 1

half = (lst[6] + lst[9] + 1) // 2

lst[6], lst[9] = half, half

print(max(lst))