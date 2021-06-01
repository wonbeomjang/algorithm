import sys

input = lambda: sys.stdin.readline()

num_dna, length = map(int, input().split())

DNAs = []

resDNA = ''
resDistance = 0

for _ in range(num_dna):
    DNAs.append(input())
    
for i in range(length):
    cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for dna in DNAs:
         cnt[dna[i]] += 1
    
    resDistance += num_dna - max(cnt.values())
    resDNA += max(cnt, key=cnt.get)
    
print(resDNA)
print(resDistance)
         