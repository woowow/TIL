'''
화살표나 백스페이스 제거
비밀번호를 알아내는 프로그램
알파벳 대소문자, 숫자, 백스페이스, 화살표
백스페이스면 -, 화살표는 <, >
백스페이스가 주어졌을때 중간에 나오면 이전것이 만약 글자면 삭제, 화살표는 커서 위치 움직이기

문자열의 길이는 100만, 즉 2중 반복문 가면 10^12, 터짐

이것도 스택을 좌우로 나눠야하나?
'''

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    password = list(sys.stdin.readline().rstrip())
    left = []
    right = []
    for chr in password: #백만
        if chr == '<':
            if left:
                right.append(left.pop())
        elif chr == '>':
            if right:
                left.append(right.pop())
        elif chr == '-':
            if left:
                left.pop()
        else:
            left.append(chr)
    
    result = "".join(left + right[::-1])

    print(result)

'''
<<BP<A>>Cd-
'''