from sys import stdin, stdout
from itertools import combinations

n, s = map(int, stdin.readline().split())
sequence = list(map(int, stdin.readline().split()))

cnt = 0

for i in range(1, len(sequence) + 1):
    for sub_seq in combinations(sequence, i):
        summation = sum(sub_seq)
        if summation == s:
            cnt += 1
        
print(cnt)