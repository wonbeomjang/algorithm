from sys import stdin

N = int(stdin.readline())

expr = []

f_1 = 0

for _ in range(N):
    coef, deg = map(int, stdin.readline().split())
    f_1 += coef * deg * (2  ** (deg - 1))
    f_1 %= (10e9 + 7)
    
print(int(f_1))