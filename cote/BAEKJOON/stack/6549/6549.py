import sys

chk = True
while chk:
    info = list(map(int, sys.stdin.readline().split()))

    N = info[0]

    if N == 0:
        break

    info.pop(0)

    

'''
히스토그램에서 가장 큰 '직사각형'의 크기
'''