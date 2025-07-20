T = int(input())

for i in range(T):
    N = int(input())
    matrix = []
    if 2 < N and N < 8:
        for j in range(N):
            temp = list(map(int, input().split()))
            matrix.append(temp)

        r90 = list(zip(*matrix[::-1]))
        r180 = [row[::-1] for row in matrix[::-1]]
        r270 = list(zip(*matrix))[::-1]

    print(f"#{i+1}")
    for i in range(len(matrix)):
        line90 = ''.join(map(str, r90[i]))
        line180 = ''.join(map(str, r180[i]))
        line270 = ''.join(map(str, r270[i]))
        print(f"{line90} {line180} {line270}")
