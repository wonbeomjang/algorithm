#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

constexpr int MAXNUM = 21;
int numRow, numCol;
char map[MAXNUM][MAXNUM];
bool alphabet['Z' - 'A' + 1];
int ans;

struct {
    int row;
    int col;
} dxdy[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};



void dfs(int row, int col, int depth) {
    ans = max(ans, depth);
    
    for(auto &p: dxdy) {
        int nextRow = row + p.row;
        int nextCol = col + p.col;
        
        if(!alphabet[map[nextRow][nextCol]]
        && 0 <= nextRow && nextRow < numRow
        && 0 <= nextCol && nextCol < numCol) {
            alphabet[map[nextRow][nextCol]] = true;
            dfs(nextRow, nextCol, depth + 1);
            alphabet[map[nextRow][nextCol]] = false;
        }
    }
    
}

int main() {
    cin >> numRow >> numCol;
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            cin >> map[i][j];
            map[i][j] -= 'A';
        }
    }
    
    
    alphabet[map[0][0]] = true;
    dfs(0, 0, 1);
    cout << ans;
}