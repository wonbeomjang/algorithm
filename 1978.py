from sys import stdin, stdout

n = int(stdin.readline())
nums = map(int, stdin.readline().split())
cnt = 0

prime = [True for i in range(1001)]
prime[1] = False
for i in range(2, 1001):
    for j in range(2, 1001):
        if not (i * j > 1000):
            prime[i * j] = False

for n in nums:
    if prime[n]:
        cnt += 1
        
print(cnt)