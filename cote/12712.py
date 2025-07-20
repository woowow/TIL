def shoot_cross(x, y, matrix, M):
    sum = matrix[x][y]
    
    for dx in range(1, M):
        if x - dx >= 0:
            sum += matrix[x-dx][y]
        if x + dx < N:
            sum += matrix[x+dx][y]

    for dy in range(1, M):
        if y - dy >= 0:
            sum += matrix[x][y-dy]
        if y + dy < N:
            sum += matrix[x][y+dy]

    return sum

def shoot_x(x, y, matrix, M):
    sum = matrix[x][y]

    for d in range(1, M):
        if x - d >= 0 and y - d >= 0:
            sum += matrix[x-d][y-d]
        if x - d >= 0 and y + d < N:
            sum += matrix[x-d][y+d]
        if x + d < N and y - d >= 0:
            sum += matrix[x+d][y-d]
        if x + d < N and y + d < N:
            sum += matrix[x+d][y+d]
    
    return sum
    
T = int(input())
 
for i in range(T):
    N, M = map(int, input().split())
     
    matrix = []
    if 4 < N and N < 16:
        if 1 < M and M < N:
            for j in range(N):
                temp = list(map(int, input().split()))
                matrix.append(temp)
#                matrix += temp

            for row in matrix:
                for val in row:
                    if val > 30:
                        exit()
            
            max_kill = float("-inf")
            
            for a in range(N):
                for b in range(N):
                    result_cross = shoot_cross(a, b, matrix, M)
                    result_x = shoot_x(a,b,matrix,M)
                    
                    max_kill = max(max_kill, result_cross, result_x)

 
    print(f"#{i+1} {max_kill}")