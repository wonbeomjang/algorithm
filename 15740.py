numTest = int(input())

inputs = []

for i in range(numTest):
    nums = input()
    num1, num2 = nums.split(' ')
    num1 = int(num1)
    num2 = int(num2)
    
    inputs += [[num1, num2]]
    
for a, b in inputs:
    print(a ** b % 10)