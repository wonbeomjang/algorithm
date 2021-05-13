from collections import deque

total_floor, cur_floor, starlink_floor, up, down = map(int, input().split())

visited = [0 for i in range(total_floor + 1)]
q = deque()

visited[cur_floor] = 1
q.append([cur_floor, 2])

while q:
    cur_floor, num_elevator = q.popleft()
    
    for next_floor in [cur_floor + up, cur_floor + down]:
        if not (0 < next_floor <= total_floor):
            continue
        
        if not visited[next_floor]:
            visited[next_floor] = num_elevator + 1
            q.append([next_floor, num_elevator + 1])

if visited[starlink_floor]:
    print(visited[starlink_floor] - 1)
else:
    print('use the stairs')
