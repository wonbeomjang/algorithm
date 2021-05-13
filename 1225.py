num1, num2 = map(list, input().split())

num1 = list(map(int, num1))
num2 = list(map(int, num2))

sum = 0

for n1 in num1:
    for n2 in num2:
        sum += n1 * n2
        
print(sum)