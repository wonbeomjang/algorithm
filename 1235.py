from sys import stdin
input = stdin.readline
num_student = int(input())

s = [set() for _ in range(101)]

for _ in range(num_student):
    number = input().rstrip()
    
    for i in range(1, len(number) + 1):
        s[i].add(number[-i:])
        
for i in range(1, 101):
    if len(s[i]) == num_student:
        print(i)
        break