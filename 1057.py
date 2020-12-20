from sys import stdin

n, kim, lim = map(int, stdin.readline().split())
res = -1


for i in range(n):
    if kim == lim:
        res = i
        break
    else:
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
        
print(res)