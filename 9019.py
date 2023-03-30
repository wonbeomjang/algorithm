import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

num_test = int(input())


def bfs(num1, num2):
    q = deque([(num1, "")])
    visited = [False] * 10000

    while q:
        num, operation = q.popleft()

        d = (2 * num) % 10000
        if d == num2: return operation + "D"
        if not visited[d]:
            q.append((d, operation + "D"))
            visited[d] = True

        s = (num - 1) % 10000
        if s == num2: return operation + "S"
        if not visited[s]:
            q.append((s, operation + "S"))
            visited[s] = True

        l = (num * 10) % 10000 + num // 1000
        if l == num2: return operation + "L"
        if not visited[l]:
            q.append((l, operation + "L"))

        r = num // 10 + (num % 10) * 1000
        if r == num2: return operation + "R"
        if not visited[r]:
            q.append((r, operation + "R"))


for _ in range(num_test):
    num1, num2 = map(int, input().split())
    print(bfs(num1, num2))

