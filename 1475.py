import sys

input = lambda: sys.stdin.readline().strip()

cnt = {}
for i in range(10):
    cnt[f'{i}'] = 0

string = list(input())

for s in string:
    cnt[s] += 1

cnt['6'] = (cnt['6'] + cnt['9'] + 1) // 2 
cnt['9'] = 0

print(max(cnt.values()))