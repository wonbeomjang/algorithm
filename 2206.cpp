#include <iostream>
#include <string.h>
#include <limits.h>
#include <algorithm>
#include <queue>
#define MAXNUM 1000
using namespace std;

bool map[MAXNUM][MAXNUM];
int depth[MAXNUM][MAXNUM][2];

int numRow, numCol;
int ans = INT_MAX;
bool flag;
char input;

struct {
    int row;
    int col;
} dxdy[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int bfs() {
    int nextRow, nextCol;
    int row, col;
    int numWalls;
    queue<pair<pair<int, int>, int>> q;
    pair<pair<int, int>, int> tuple;
    pair<int, int> point;
    
    q.push({{0, 0}, 0});
    depth[0][0][0] = 1;
    
    while(!q.empty()) {
        tuple = q.front();
        point = tuple.first;
        numWalls = tuple.second;
        
        q.pop();
        
        row = point.first;
        col = point.second;
        
        
        if (row == numRow - 1 && col == numCol - 1) return depth[row][col][numWalls];
        
        for(auto &i: dxdy) {
            nextRow = row + i.row;
            nextCol = col + i.col;
            if(0 <= nextRow && nextRow < numRow
            && 0 <= nextCol && nextCol < numCol
            && !depth[nextRow][nextCol][numWalls]) {
                // 벽이고 아직 벽을 안 부셨을 때
                if(map[nextRow][nextCol] == 1 && numWalls == 0) {
                    depth[nextRow][nextCol][numWalls + 1] = depth[row][col][numWalls] + 1;
                    q.push({{nextRow, nextCol}, numWalls + 1});
                }
                // 지나갈 수 있을 때
                else if (map[nextRow][nextCol] == 0) {
                    depth[nextRow][nextCol][numWalls] = depth[row][col][numWalls] + 1;
                    q.push({{nextRow, nextCol}, numWalls});
                }
            }
        }
    }
    
    return -1;
}


int main() {
    cin >> numRow >> numCol;
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            cin >> input;
            map[i][j] = input - '0';
        }
    }
    
    cout << bfs();
}