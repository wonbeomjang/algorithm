import sys

input = lambda: sys.stdin.readline().strip()

def diff(str1, str2):
    return sum((s1 != s2 for s1, s2 in zip(str1, str2)))
    
str1, str2 = input().split()

len_diff = len(str2) - len(str1)

res = 100
for i in range(0, len_diff + 1):
    res = min(res, diff(str1, str2[i: i + len(str1)]))

print(res)