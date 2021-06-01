import operator
import sys

input = lambda: sys.stdin.readline().strip()


N = int(input())
num_vote = {}

for i in range(1, N + 1):
    num_vote[i] = int(input())
 
ans = 0

while True:
    max_key = max(num_vote, key=num_vote.get)
    
    if max_key == 1:
        break
    
    num_vote[max_key] -= 1
    num_vote[1] += 1
    
    ans += 1

print(ans)