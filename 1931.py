import sys

input = lambda: sys.stdin.readline().strip()

num_meeting = int(input())

schedule = []
for _ in range(num_meeting):
    start, end = map(int, input().split())
    schedule += [(start, end)]

schedule.sort()
schedule.sort(key = lambda x: x[1])

end = 0
res = 0

for s, e in schedule:
    if end <= s:
        res += 1
        end = e

print(res)