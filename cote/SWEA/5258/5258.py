import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())


    lst = []
    
    for i in range(M):
        S, P = map(int, input().split())
        lst.append((S, P))





