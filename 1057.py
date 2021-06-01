import sys

input = lambda: sys.stdin.readline().strip()

num_people, p1, p2 = map(int, input().split())
p1 -= 1
p2 -= 1

res = -1

for i in range(num_people):
    if p1 == p2:
        res = i
        break
    
    p1 //= 2
    p2 //= 2
    
print(res)