#include <iostream>
#include <queue>
using namespace std;

constexpr int maxNum = 501;

struct {
    int row;
    int col;
} dxdy[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

int numRow, numCol;
int map[maxNum][maxNum];
int dp[maxNum][maxNum];
bool visited[maxNum][maxNum];

int dfs(int row, int col) {
    int nextRow, nextCol;
    
    if (visited[row][col]) return dp[row][col];
    if (row == 0 && col == 0) return 1;

    dp[row][col] = 0;
    
    for(auto &p: dxdy) {
        nextRow = row + p.row;
        nextCol = col + p.col;
        if(0 <= nextRow && nextRow < numRow
        && 0 <= nextCol && nextCol < numCol
        && map[nextRow][nextCol] > map[row][col]) {
            visited[row][col] = true;
            dp[row][col] += dfs(nextRow, nextCol);
        }
    }
    
    return dp[row][col];
}

int main() {
    cin >> numRow >> numCol;
    
    for (int i = 0; i < numRow; i++) {
        for (int j = 0; j < numCol; j++) {
            cin >> map[i][j];
        }
    }
    
    dp[0][0] = 1;
    
    cout << dfs(numRow - 1, numCol - 1) ;
    
}