import sys
from collections import Counter

input = lambda: sys.stdin.readline().strip()

num = Counter(input())

center = ''
for n in num:
    if num[n] % 2:
        center += n
        
if len(center) > 1:
    print("I'm Sorry Hansoo")
    sys.exit(0)
    

num = sorted(num.items())

string = ''
for a, n in num:
    string += a * (n // 2)

print(string + center + string[::-1])
    
