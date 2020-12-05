inputs = input()

nums = inputs.split('-')

res = nums.pop(0)

sum = 0
for n in res.split('+'):
    sum += int(n)
res = sum

for expr in nums:
    sum = 0;
    for n in expr.split('+'):
        sum += int(n)
    res -= sum

print(res)