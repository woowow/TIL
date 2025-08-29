import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = sys.stdin.readline().rstrip()
    M = sys.stdin.readline().rstrip()

    # 무조건 N을 M보다 짧은걸로
    if len(N) > len(M):
        temp = M.copy()
        M = N
        N = temp
    
    if N in M:
        result = 1
    else:
        result = 0
    
    print(f"#{tc} {result}")