import sys
from collections import deque

input = lambda:sys.stdin.readline().strip()

i = 0

while True:
    string = input()
    if string == '---':
        break
    i += 1
    cnt = 0
    stack = []
    for s in list(string):
        if not stack and s == '}':
            cnt += 1
            stack.append('{')
        elif stack and s == '}':
            stack.pop()
        else:
            stack.append(s)
    
    cnt += len(stack) // 2
    ans +=