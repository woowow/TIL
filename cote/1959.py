T = int(input())
 
for i in range(T):
    N, M = map(int, input().split())
     
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    if N > M:
        A, B = B, A
        N, M = M, N
     
    max_val = float("-inf")
    for j in range(M-N+1):
        sum = 0
        for k in range(N):
            sum += A[k] * B[k+j]
 
        if max_val < sum:
            max_val = sum
 
    print(f"#{i+1} {max_val}")