length, num_erase = map(int, input().split())
number = list(input())
exclude_number = list(range(len(number)))
exclude_number.sort(key=lambda x: (number[x], -x))
exclude_number = set(exclude_number[:num_erase])
res = ""

for i in range(len(number)):
    if i not in exclude_number:
        res += number[i]
print(res)