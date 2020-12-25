from sys import stdin, stdout

N, S = map(int, stdin.readline().split())
pop_nums = map(int, stdin.readline().split())

queue = [i for i in range(1, N + 1)]
start = 0
dap = 0
for n in pop_nums:
    cnt = 0
    
    while queue[start] != n:
        start = (start + 1) % len(queue)
        cnt += 1
        
    dap += min(cnt, len(queue) - cnt)
    queue.pop(start)
    
    if queue:
        start = (start) % len(queue)
    
stdout.write(f'{dap}')