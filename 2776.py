num_tests = int(input())

for i in range(num_tests):
    input()
    num1 = set(input().split())
    
    input()
    num2 = input().split()
    
    for n in num2:
        print(1 if n in num1 else 0)