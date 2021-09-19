import sys
from collections import deque
from itertools import chain

input = lambda: sys.stdin.readline().strip()
dndi = ((1, 0), (0, 1), (-1, 0), (0, -1))

num_plates, num_integers, num_rotations = map(int, input().split())
plates = [list(map(int, input().split())) for i in range(num_plates)]
commands = [map(int, input().split()) for i in range(num_rotations)]


CLOCKWISE = 0
COUNTERCLOCKWISE = 1

def rotate(plate, direction, distance):
    if direction == COUNTERCLOCKWISE:
        return plate[distance:] + plate[:distance]
    elif direction == CLOCKWISE:
        return plate[-distance:] + plate[:-distance]
    else:
        raise Exception("Error")

def bfs(plates, n, i):
    q = deque()
    q.append((n, i))
    visited = set()
    visited.add((n, i))
    
    value = plates[n][i]
    
    while q:
        n, i = q.popleft()
         
        for dn, di in dndi:
            next_n = n + dn
            next_i = (i + di) % num_integers
            
            if not 0 <= next_n < num_plates:
                continue
            
            if (next_n, next_i) in visited:
                continue
            
            if value == plates[next_n][next_i]:
                q.append((next_n, next_i))
                visited.add((next_n, next_i))
    
    return visited
    
def find(plates):
    flag = False
    
    for n in range(num_plates):
        for i in range(num_integers):
            if plates[n][i]:
                adj = bfs(plates, n, i)
                if len(adj) > 1:
                    flag = True
                    
                    for n0, i0 in adj:
                        plates[n0][i0] = 0
                        
    if not flag and [i for i in chain(*plates) if i != 0]:
        avg = sum(chain(*plates)) / len([i for i in chain(*plates) if i != 0])
        
        for n in range(num_plates):
            for i in range(num_integers):
                if plates[n][i]:
                    if plates[n][i] > avg:
                        plates[n][i] -= 1
                    elif plates[n][i] < avg:
                        plates[n][i] += 1
                        
    return plates


for x, d, k in commands:
    for n in range(num_plates):
        if (n + 1) % x == 0:
            plate = plates[n]
            plates[n] = rotate(plate, d, k)
    
    plates = find(plates)
    
print(sum(chain(*plates)))