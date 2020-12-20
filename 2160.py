from sys import stdin
from itertools import combinations

def cal_diff(pic1, pic2):
    cnt = 0
    for i_1, i_2 in zip(pic1, pic2):
        for j_1, j_2 in zip(i_1, i_2):
            if j_1 != j_2:
                cnt += 1
    return cnt
            
n = int(stdin.readline())

pictures = []

for i in range(n):
    pic = []
    for _ in range(5):
        pic += [list(stdin.readline())]
    
    pictures += [pic]

min_diff = 5 * 7
min_pic1 = 0
min_pic2 = 0

for i, j in combinations(range(n), 2):
    diff = cal_diff(pictures[i], pictures[j])
    if min_diff > diff:
        min_diff = diff
        min_pic1 = i
        min_pic2 = j
        
i, j = sorted([min_pic1 + 1, min_pic2 + 1])

print(f'{i} {j}')