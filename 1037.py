from sys import stdin

stdin.readline()
divisors = list(map(int, stdin.readline().split()))

divisors.sort()

print(divisors[0] * divisors[-1])
