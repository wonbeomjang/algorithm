import re

n = input()


if re.match("9+", n):
    print(int(n) + 2)
elif len(n) % 2 == 1:
    half = str(int(n[:len(n)//2 + 1]) + 1)
    print(half + half[::-1][1:])
else:
    half = str(int(n[:len(n)//2]) + 1)
    print(half + half[::-1])

