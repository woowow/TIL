import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a_i = list(map(int, input().split()))

    a_i = sorted(a_i)

    print(f"#{tc} {a_i[N//2]}")