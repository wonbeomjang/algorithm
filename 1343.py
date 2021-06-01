board = input()

board = board.replace('XXXX', 'AAAA').replace('XX', 'BB')


if board.find('X') == -1:
    print(board)
else:
    print(-1)
