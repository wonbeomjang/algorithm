import sys

input = lambda: sys.stdin.readline().strip()

# num_bridge = int(input())
num_bridge = 10

def get_num_jump(dis):
    cur_pos = dis
    cnt = 0
    
    while cur_pos <= num_bridge:
        print(cur_pos)
        cnt += 1
        if cur_pos == num_bridge:
            return cnt
            
        dis += 1
        cur_pos += dis
    
    return cnt - 1

print(get_num_jump(1))
print()
print(get_num_jump(2))
print()
print(get_num_jump(3))
print()
print(get_num_jump(4))
    