from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([a, ''])
    
    while q:
        number, result = q.popleft()
        
        d = (2 * number) % 10000
        if d == b: return result + 'D'
        elif not visited[d]:
            visited[d] = True
            q.append([d, result + 'D'])
        
        s = number - 1 if number != 0 else 9999
        if s == b: return result + 'S'
        elif not visited[s]:
            visited[s] = True
            q.append([s, result + 'S'])
        
        l = int(number % 1000 * 10 + number / 1000)
        if l == b: return result + 'L'
        elif not visited[l]:
            visited[l] = True
            q.append([l, result + 'L'])
        
        r = int(number % 10 * 1000 + number // 10)
        if r == b: return result + "R"
        elif not visited[r]:
            visited[r] = True
            q.append([r, result + "R"])


num_test = int(input())
for i in range(num_test):
    a, b = map(int, input().split())
    
    visited = [False for _ in range(10000)]
    print(bfs())
    