import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    
    cnt = 0

    cnt_b = A.count(B)

    cnt = len(A) - (cnt_b*len(B)) + cnt_b

    # while B in A:
    #     A = A.replace(B, "", 1)
    #     cnt += 1
    # '''
    # A 안에 B를 모두 삭제할 때까지 반복
    # 삭제할 때마다 cnt += 1
    # '''
    # cnt += len(A)

    print(f"#{tc} {cnt}")

