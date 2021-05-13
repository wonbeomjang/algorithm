num_row, num_col = map(int, input().split())

source_matrix = [list(map(int, list(input()))) for _ in range(num_row)]
target_matrix = [list(map(int, list(input()))) for _ in range(num_row)]

def flip(matrix, row, col):
    for i in range(3):
        for j in range(3):
                matrix[row + i][col + j] = (matrix[row + i][col + j] + 1) % 2

def check(m1, m2):
    for i in range(num_row):
        for j in range(num_col):
            if m1[i][j] != m2[i][j]:
                return False
    return True

cnt = 0

for i in range(num_row - 2):
    for j in range(num_col - 2):
        if source_matrix[i][j] != target_matrix[i][j]:
            cnt += 1
            flip(source_matrix, i, j)

if check(source_matrix, target_matrix):
    print(cnt)
else:
    print(-1)