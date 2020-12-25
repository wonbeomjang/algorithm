N = int(input())

expr = input()
max_num = -(2 ** 31)

def dfs(index, cur_val):
    global expr
    global max_num
    
    if index > N - 1:
        max_num = max(max_num, cur_val)
        return
    
    op = '+' if index == 0 else expr[index - 1]
    
    if index + 2 < N:
        dfs(index + 4, eval(f'{cur_val}{op}({expr[index: index + 3]})'))
    
    dfs(index + 2, eval(f'{cur_val}{op}{expr[index]}'))
   
        
dfs(0, 0)
print(max_num)