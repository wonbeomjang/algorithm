dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

DIR = {'E': 0, 'N': 1, 'W': 2, 'S': 3}

EAST = 0
NOTRH = 1
WEST = 2
SOUTH = 3

width, height = map(int, input().split())
num_robots, num_command = map(int, input().split())

robots = [[0, 0, 0]]
board = {}

for i in range(1, num_robots + 1):
    x, y, dir = input().split()
    robots += [[int(x), int(y), DIR[dir]]]
    board[f'{x}_{y}'] = i

done = False
commands = [input().split() for i in range(num_command)]


for i in range(num_command):
    if done:
        break
    
    num, command, repeat = commands[i]
    num = int(num)
    repeat = int(repeat)
    
    for i in range(repeat):
        x, y, dir = robots[num]
        
        if command == 'L':
            dir = (dir + 1) % 4
            robots[num] = [x, y, dir]
        elif command == 'R':
            dir = (dir + 3) % 4
            robots[num] = [x, y, dir]
        else:
            nx = x + dxdy[dir][0]
            ny = y + dxdy[dir][1]
            if not (0 < nx <= width and 0 < ny <= height):
                print(f'Robot {num} crashes into the wall')
                done = True
                break
            
            elif f'{nx}_{ny}' in board:
                print(f"Robot {num} crashes into robot {board[f'{nx}_{ny}']}")
                done = True
                break
            
            else:
                robots[num] = [nx, ny, dir]
                board.pop(f'{x}_{y}')
                board[f'{nx}_{ny}'] = num
            
if not done:
    print('OK')