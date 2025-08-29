import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    nums_asc = sorted(nums)
    nums_desc = sorted(nums, reverse=True)


    result = []
    ran = 0
    if N > 10:
        ran = 5
    else:
        ran = N//2
    for i in range(ran):
        result.append(nums_desc[i])
        result.append(nums_asc[i])

    print(f'#{tc}', *result)