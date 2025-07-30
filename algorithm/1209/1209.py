import sys
import numpy as np
# open을 사용해서 input.txt 파일 열기
sys.stdin = open('input.txt')

# 10개의 테스트 케이스
for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    max = 0

    print(f"#{tc} {max}")
    