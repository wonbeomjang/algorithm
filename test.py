from collections import deque

SUSPANDED = 1
VISITED = 2
NOT_VISITED = 0

def bfs(graph, order, not_visit, n):
    q = deque()
    visited = [0] * n
    
    q.append(0)
    visited[0] = True
    
    while q:
        v = q.popleft()
        
        if not_visit[v]:
            visited[v] = SUSPANDED
        
        for n_v in graph[v]:
            print(visited)
            if visited[n_v] is NOT_VISITED:
                
                visited[n_v] = VISITED
                q.append(n_v)
                
                if visited[order[n_v]] is SUSPANDED:
                    not_visit[order[n_v]] = 0
                    visited[order[n_v]] = VISTED
                    q.append(order[n_v])
                
    for i in visited:
        if i == 0:
            return False
    return True
                

def solution(n, path, temp_order):
    graph = [[] for _ in range(n)]
    order = [0 for _ in range(n)]
    not_visit = [0 for _ in range(n)]
    
    for start, end in path:
        graph[start] += [end]
    
    for start, end in temp_order:
        order[start] = end
        not_visit[end] = start
    
    answer = bfs(graph, order, not_visit, n)
    
    
    return answer
    


print(solution(	9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))