from sys import stdin

n, m = map(int, stdin.readline().split())

money = []

for i in range(n):
    money += [int(stdin.readline())]
    
def numWithdrawal(amount: int):
    global money
    cnt = 0
    temp = 0
    
    for m in money:
        if m > amount:
            return 100001
        elif temp < m:
            temp = amount
            cnt += 1
        
        temp -= m
            
    return cnt
            

left = 0
right = sum(money)

while left <= right:
    mid = (left + right) // 2
    if m < numWithdrawal(mid):
        left = mid + 1;
    else:
        right = mid - 1

print(left)