def check(errors: list, num: int) -> bool:
    if num < 0:
        return False
        
    num = str(num)
    for n in num:
        if int(n) in errors:
            return False
        
    return True

find = False
target_num = int(input())
num_error = int(input())

err = list(map(int, input().split(' ')))

minimum = 600001

for test_num in range(1000000):
    if check(err, test_num):
        minimum = min(minimum, len(str(test_num)) + abs(target_num - test_num))
    if test_num == 100:
        minimum = min(minimum, abs(target_num - test_num))
print(minimum)