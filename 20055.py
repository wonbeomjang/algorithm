import sys
from collections import deque

n, k = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([False] * n)
stage = 0

while True:
    durability.rotate(1)
    robot.rotate(1)
    robot[-1] = False
    
    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and durability[i + 1] > 0:
            robot[i], robot[i + 1] = False, True
            durability[i + 1] -= 1
            
    robot[-1] = False
        
    if not robot[0] and durability[0] > 0:
        robot[0] = True
        durability[0] -= 1
    
    stage += 1
    if durability.count(0) >= k:
        break

print(stage)