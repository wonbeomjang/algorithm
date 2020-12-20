from sys import stdin
from itertools import combinations

def is_palindrome(string: str) -> bool:
    start = 0
    end = len(string) - 1
    
    while start < end:
        if string[start] != string[end]:
            return False
            
        start += 1
        end -= 1
            
    return True

string = input()
length = len(string)

for i in range(length):
    if is_palindrome(string[i:]):
        print(length + i)
        break
else:
    print(length * 2)
