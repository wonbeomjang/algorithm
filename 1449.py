from sys import stdin, stdout

n, l = map(int, stdin.readline().split())
lick_point = sorted(map(int, stdin.readline().split()))
cnt = 1

start = lick_point[0]
end = lick_point[0] + l

for p in lick_point:
    if start <= p < end:
        continue
    else:
        cnt += 1
        start = p
        end = p + l
        
print(cnt)