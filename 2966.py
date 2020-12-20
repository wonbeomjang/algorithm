from sys import stdin

n = int(stdin.readline())
answer = list(stdin.readline())

Adrian_score = 0
Bruno_score = 0
Goran_score = 0
    
for i in range(n):
    if answer[i] == ['A', 'B', 'C'][i % 3]:
        Adrian_score += 1
    if answer[i] == ['B', 'A', 'B', 'C'][i % 4]:
        Bruno_score += 1
    if answer[i] == ['C', 'C', 'A', 'A', 'B', 'B'][i % 6]:
        Goran_score += 1
        
max_score = max({Adrian_score, Bruno_score, Goran_score})
print(max_score)
if max_score == Adrian_score:
    print('Adrian')
if max_score == Bruno_score:
    print('Bruno')
if max_score == Goran_score:
    print('Goran')