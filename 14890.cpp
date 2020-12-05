#include <iostream>
using namespace std;

int map[100][100];
const int leftRight = 0;
const int topDown = 1;

int N, L;

bool dfs(int row, int col, int dir) {
    
    if(row == N - 1 || col == N - 1) return true;
    
    if (dir == leftRight) {
        for(int i = 1; i < L && col + i < N; i++) 
            if (map[row][col] != map[row][col + i]) 
                return false;
                
        if(map[row][col] + 1 == map[row][col + L] && col + L < N) 
            return dfs(row, col + L, dir);
        
        
        if(map[row][col] == map[row][col + L] + 1 && col + L < N) 
            return dfs(row, col + L, dir);
            
        else if (map[row][col] == map[row][col + 1] && col + 1 < N)
            return dfs(row, col + 1, dir);
        else
            return false;
    }
    else {
        for(int i = 1; i < L && row + i < N; i++)
            if (map[row][col] != map[row + i][col]) 
                return false;
                
        if(map[row][col] + 1 == map[row + L][col] && row + L < N)
            return dfs(row + L, col, dir);
                
        if(map[row][col] == map[row + L][col] + 1 && row + L < N)
            return dfs(row + L, col, dir);
            
        else if (map[row][col] == map[row + 1][col] && row + 1 < N)
            return dfs(row + 1, col, dir);
        else
            return false;
    
    }
    
    return true;
}

int main() {
    int res = 0;
    cin >> N >> L;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
        }
    }
    
    for (int i = 0; i < N; i++)
        if (dfs(i, 0, leftRight)) 
            res++;
    
    for (int i = 0; i < N; i++)
        if (dfs(0, i, topDown)) 
            res++;
            
    cout << res;
}