arr = []
for i in range(1, 46):
    arr += [i] * i

start, end = map(int, input().split())
print(sum(arr[start - 1: end]))
