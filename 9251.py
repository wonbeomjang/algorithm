str1 = input()
str2 = input()

table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for idx1, char1 in enumerate(str1, 1):
    for idx2, char2 in enumerate(str2, 1):
        if char1 == char2:
            table[idx1][idx2] = table[idx1 - 1][idx2 - 1] + 1
        else:
            table[idx1][idx2] = max(table[idx1 - 1][idx2], table[idx1][idx2 - 1])
            
print(table[-1][-1])
    
    
    