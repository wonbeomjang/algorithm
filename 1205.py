import sys
from collections import Counter

input = lambda: sys.stdin.readline().strip()

num_score, new_score, limit = map(int, input().split())
scores = list(map(int, input().split()))
scores += [new_score]
scores = sorted(scores, reverse=True)

rank = scores.index(new_score) + 1

if rank > limit or (scores[-1] == new_score and num_score == limit):
    rank = -1

print(rank)
