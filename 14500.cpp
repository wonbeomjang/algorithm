#include <iostream>
#include <algorithm>
using namespace std;

constexpr int maxNum = 501;

int numRow, numCol;
int map[maxNum][maxNum];
bool visited[maxNum][maxNum];

struct {
    int row;
    int col;
} dxdy[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

int dfs(int row, int col, int depth) {
    if(depth == 4) return map[row][col];
    
    int nextRow, nextCol;
    int maxNum = 0;
    
    for(auto &p: dxdy) {
        nextRow = row + p.row;
        nextCol = col + p.col;
        
        if(!visited[nextRow][nextCol]
        && 0 <= nextRow && nextRow < numRow
        && 0 <= nextCol && nextCol < numCol) {
            visited[nextRow][nextCol] = true;
            maxNum = max(maxNum, map[row][col] + dfs(nextRow, nextCol, depth + 1));
            visited[nextRow][nextCol] = false;
        }
    }
    
    return maxNum;
}

int fingerShape(int row, int col) {
    int maxNum = 0;
    // ㅏ
    if (0 <= row - 1 && row + 1 < numRow && col + 1 < numCol)
        maxNum = max(maxNum, map[row - 1][col] + map[row][col] + map[row + 1][col] + map[row][col + 1]);
    // ㅓ
    if (0 <= row - 1 && row + 1 < numRow &&  0 <= col - 1)
        maxNum = max(maxNum, map[row - 1][col] + map[row][col] + map[row + 1][col] + map[row][col - 1]);
    // ㅜ
    if (0 <= col - 1 && col + 1 < numCol && row + 1 < numRow)
        maxNum = max(maxNum, map[row][col - 1] + map[row][col] + map[row][col + 1] + map[row + 1][col]);
    // ㅗ
    if (0 <= col - 1 && col + 1 < numCol &&  0 <= row - 1)
        maxNum = max(maxNum, map[row][col - 1] + map[row][col] + map[row][col + 1] + map[row - 1][col]);
    return maxNum;
}

int main() {
    cin >> numRow >> numCol;
    int maxNum = 0;
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            cin >> map[i][j];
        }
    }
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            visited[i][j] = true;
            maxNum = max(maxNum, dfs(i, j, 1));
            maxNum = max(maxNum, fingerShape(i, j));
            visited[i][j] = false;
        }
    }
    
    cout << maxNum;
}