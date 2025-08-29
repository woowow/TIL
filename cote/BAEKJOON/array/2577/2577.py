A = int(input())
B = int(input())
C = int(input())

total = A * B * C

for num in '0123456789':
    cnt = str(total).count(num)
    print(cnt)