alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
nums = ['X', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
command = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
king_pos, rock_pos, n = input().split()

king_pos = [alphabet[king_pos[0]], int(king_pos[1])]
rock_pos = [alphabet[rock_pos[0]], int(rock_pos[1])]

commands = []
n = int(n)
for i in range(n):
    commands += [input()]

for c in commands:
    dx, dy = command[c]
    king_x, king_y = king_pos
    rock_x, rock_y = rock_pos
    
    next_king_x = king_x + dx
    next_king_y = king_y + dy
    
    next_rock_x = rock_x + dx
    next_rock_y = rock_y + dy
    
    if 0 < next_king_x <= 8 and 0 < next_king_y <= 8:
        if next_king_x == rock_x and next_king_y == rock_y:
            if 0 < next_rock_x <= 8 and 0 < next_rock_y <= 8:
                rock_x = next_rock_x
                rock_y = next_rock_y
            else:
                continue
        king_x = next_king_x
        king_y = next_king_y
    else:
        continue
    
    king_pos = [king_x, king_y]
    rock_pos = [rock_x, rock_y]
    
print(f'{nums[king_pos[0]]}{king_pos[1]}')
print(f'{nums[rock_pos[0]]}{rock_pos[1]}')