import sys

input = lambda: sys.stdin.readline().strip()

num_books, max_num = map(int, input().split())
positions = list(map(int, input().split()))

minus = sorted([abs(x) for x in positions if x < 0])
plus = sorted([x for x in positions if x >= 0])

first_list = list(reversed(minus if minus[-1] < plus[-1] else plus))
second_list = plus if minus[-1] < plus[-1] else minus

class Player:
    movement = 0
    cur_pos = 0
    def __init__(self, max_carry):
        self.max_carry = max_carry
        self.num_carry = max_carry
        
    def move(self, pos):
        if not self.num_carry:
            self.set_pos_zero()
            
        self.num_carry -= 1
        self.movement += abs(pos - self.cur_pos)
        self.cur_pos = pos
    
    def set_pos_zero(self):
        self.movement += self.cur_pos
        self.cur_pos = 0
        self.num_carry = self.max_carry
    
player = Player(max_num)

for f in first_list:
    player.move(f)
player.set_pos_zero()

if len(second_list) % max_num:
    while len(second_list) % max_num:
        player.move(second_list[0])
        del second_list[0]
player.set_pos_zero()

for s in second_list:
    player.move(s)

print(player.movement)

