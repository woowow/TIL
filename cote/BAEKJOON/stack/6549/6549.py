import sys
from collections import deque

while True:
    hist = deque(list(map(int, sys.stdin.readline().split())))

    n = hist.popleft()
    if n == 0:
        break

    max_extent = 0

    stack = []

    for i, h in enumerate(hist):
        start = i

        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_extent = max(max_extent, height*(i - idx))
            start = idx
        stack.append((start, h))

    for i, h in stack:
        max_extent = max(max_extent, h * (n - i))
    
    print(max_extent)

