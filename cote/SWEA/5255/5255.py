import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tiles = [0] * (N+1)
    tiles[1] = 1
    tiles[2] = 3
    tiles[3] = 6
    for i in range(4, N+1):
        tiles[i] = tiles[i-1] + 2*tiles[i-2] + tiles[i-3]

    print(f"#{tc} {tiles[N]}")


'''
2x1
1
2x2
3
2x3
6
2x4
13

3개로 구성된거에 tile 하나 붙이는거잖아


'''