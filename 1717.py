import sys

input = sys.stdin.readline

def find_parent(target):
    if parent[target] == target:
        return target
    
    parent[target] = find_parent(parent[target])
    return parent[target]

def union(num1, num2):
    num1 = find_parent(num1)
    num2 = find_parent(num2)
    
    if num1 != num2:
        parent[num2] = num1
    

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for i in range(m):
    op, num1, num2 = map(int, input().split())
    
    if op == 0:
        union(num1, num2)
    else:
        if find_parent(num1) == find_parent(num2):
            print('YES')
        else:
            print('NO')
