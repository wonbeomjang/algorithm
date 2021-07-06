import sys

input = lambda: sys.stdin.readline().strip()
# print = sys.stdout.write

num_tests = int(input())

for i in range(num_tests):
    procedure = list(input())
    num_arr = int(input())
    arr = input()[1:-1].split(',')
    
    if not num_arr: 
        arr = []
        
    if len(arr) < procedure.count('D'):
        print('error')
        continue
    
    
    left = True
    
    for p in procedure:
        if 'R' == p:
            left = not left
            
        elif 'D' == p:
            if left:
                del arr[0]
            else:
                del arr[-1]
    if left:
        content = ','.join(arr)
    else:
        content = ','.join(reversed(arr))
        
    print(f'[{content}]')