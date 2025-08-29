import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def combination(n, r):
    if r > n - r:
        r = n - r
    result = 1
    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)

    return result
    

for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    
    coef = [0] * (n+1)
    coef[0] = 1
    coef[n] = 1
        
    for i in range(1, n):
        coef[i] = combination(n, i)
    
    print(coef)
    print(f"#{tc} {coef[a]}")
    

'''
combination이네
(x+y)^2 = x^2 + 2xy + y^2
(x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3
(x+y)^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4
(x+y)^5 = x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5
'''