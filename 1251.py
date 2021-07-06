from itertools import combinations
import sys

input = lambda: sys.stdin.readline().strip()

string = input()

res = "z"*len(string)

for i, j in combinations(range(1, len(string)), 2):
    str1 = string[:i]
    str2 = string[i:j]
    str3 = string[j:]
    new_string = str1[::-1] + str2[::-1] + str3[::-1]
    res = new_string if res > new_string else res
    
print(res)
