from sys import stdin

n = int(stdin.readline())

length = len(str(n))
max_diff = length * 9
print_num = 0

for cur_m in range(1, n + 1):
    expect_n = cur_m
    
    expect_n += sum(list(map(int, str(cur_m))))
    
    if expect_n == n:
        print_num = cur_m
        break

print(print_num)