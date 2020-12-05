from itertools import combinations
from itertools import permutations

N = int(input())
res = 100 * 20 * 20 * 10
ability = []

for _ in range(N):
    ability += [list(map(int, input().split(' ')))]

for team_1 in combinations(range(N), N // 2):
    team_1 = set(team_1)
    team_2 = set(range(N)) - set(team_1)
    
    team_1_ability = 0
    for m1, m2 in permutations(team_1, 2):
        team_1_ability += ability[m1][m2]
    
    team_2_ability = 0
    for m1, m2 in permutations(team_2, 2):
        team_2_ability += ability[m1][m2]
    
    diff = abs(team_1_ability - team_2_ability)
    
    if diff < res:
        res = diff

print(res)