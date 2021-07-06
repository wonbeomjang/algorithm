import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

start = list(input())
target = list(input())

while len(start) != len(target):
    if not target[-1] == 'A':
        target.pop()
        target = target[::-1]
    else:
        target.pop()
        
print(1 if start == target else 0)