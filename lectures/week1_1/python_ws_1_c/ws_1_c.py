# 아래에 코드를 작성하시오.

def soldout(x,y):
    theater[x][y] = 'X'

theater = [['O' for _ in range(3)] for _ in range(3)]

soldout(0,2)
soldout(1,0)
soldout(1,2)
soldout(2,0)
soldout(2,2)

print("현재 좌석 배치:")
for row in theater:
    print(' '.join(row))