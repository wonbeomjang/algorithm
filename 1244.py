from sys import stdin

input = stdin.readline

num_switch = int(input())
switch_state = list(map(int, input().split()))

num_student = int(input())

def man(pos):
    global switch_state
    
    for i in range(len(switch_state)):
        if (i + 1) % pos == 0:
            switch_state[i] = (switch_state[i] + 1) % 2
            
def woman(pos):
    pos -= 1
    for i in range(1, len(switch_state)):
        start = pos - i
        end = pos + i
        
        if start < 0 or len(switch_state) <= end:
            start += 1
            end -=1
            break
        
        if switch_state[start] != switch_state[end]:
            start += 1
            end -=1
            break
        
    for i in range(start, end + 1):
        switch_state[i] = (switch_state[i] + 1) % 2

for _ in range(num_student):
    gender, pos = map(int, input().split())
    
    if gender == 1:
        man(pos)
    else:
        woman(pos)

for i, n in enumerate(switch_state):
    if i % 20 == 0 and i != 0:
        print()
    print(n, end=' ')