import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    max_val = 0
    for chr in str1:
        temp = str2.count(chr)
        max_val = max(max_val, temp)
    
    print(f"#{tc} {max_val}")