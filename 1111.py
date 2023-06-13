n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
else:
    if arr[1] - arr[0] == 0:
        a = 0
    else:
        a = (arr[2] - arr[1]) // (arr[1] - arr[0])
    b = arr[1] - a * arr[0]

    for i in range(n - 1):
        if arr[i + 1] != a * arr[i] + b:
            print("B")
            break
    else:
        print(a * arr[n - 1] + b)
