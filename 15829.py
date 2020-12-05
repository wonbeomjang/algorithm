L = int(input())

string = input()

r = 31
M = 1234567891

res = 0

for i in range(L):
    a = ord(string[i]) - 96
    res += (a * (r ** i))  % M
    
print(res)