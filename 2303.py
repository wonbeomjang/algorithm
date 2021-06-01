import sys
from itertools import combinations

input = lambda: sys.stdin.readline().strip()

def dfs(card, pos, depth, max_num):
    if depth == 3:
        return card[pos]
    
    for i in range(pos + 1, len(card)):
        res = card[pos] + dfs(card, i, depth + 1)
        
        if (max_num % 10) < (res % 10):
            max_num = res
        elif (max_num % 10) == (res % 10):
            if max_num < res:
                
        

num_people = int(input())
res = []

for i in range(1, num_people + 1):
    cards = map(int, input().split())
    nums = []
    
    