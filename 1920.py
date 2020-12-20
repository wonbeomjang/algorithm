def binary_search(arr: list, target: int):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0

input()
nums = sorted(map(int, input().split()))
input()
find = map(int, input().split())

for f in find:
    print(binary_search(nums, f))
