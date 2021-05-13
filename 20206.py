A, B, C = map(int, input().split())
X_1, X_2, Y_1, Y_2 = map(int, input().split())

xy = ((X_1, Y_1), (X_2, Y_1), (X_1, Y_2), (X_2, Y_2))

res = []

for x, y in xy:
    res += [A * x + B * y + C]

if res[0] <= 0 and res[1] <= 0 and res[2] <= 0 and res[3] <= 0:
    print('Lucky')
elif res[0] >= 0 and res[1] >= 0 and res[2] >= 0 and res[3] >= 0:
    print('Lucky')
else:
    print('Poor')