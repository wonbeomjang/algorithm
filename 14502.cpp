#include <iostream>
#include <string.h>
#include <algorithm>
#include <queue>
#define MAXSIZE 8
using namespace std;

struct {
    int row;
    int col;
} dxdy[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int numRow;
int numCol;

int map[MAXSIZE][MAXSIZE];
int tempMap[MAXSIZE][MAXSIZE];

int spreadVirus() {
    int N = numRow, M = numCol;
    memcpy(tempMap, map, sizeof(int) * MAXSIZE * MAXSIZE);

    queue<pair<int, int>>q;
    pair<int, int> point;
    int nextRow, nextCol;
    int row, col;
    int numFreeSpace = 0;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(tempMap[i][j] == 2)
                q.push(make_pair(i, j));
        }
    }

    while (!q.empty()) {
        point = q.front();
        row = point.first;
        col = point.second;
        q.pop();

        for(auto &i: dxdy) {
            nextRow = row + i.row;
            nextCol = col + i.col;
            if(tempMap[nextRow][nextCol] == 0
            && 0 <= nextRow && nextRow < N
            && 0 <= nextCol && nextCol < M) {
                tempMap[nextRow][nextCol] = 2;
                q.push(make_pair(nextRow, nextCol));
            }
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(tempMap[i][j] == 0) {
                numFreeSpace++;
            }
        }
    }


    return numFreeSpace;
}


int spread() {
    memcpy(tempMap, map, sizeof(int) * MAXSIZE * MAXSIZE);
    
    queue<pair<int, int>> q;
    pair<int, int> point;
    int row, col;
    int nextRow, nextCol;
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            if(tempMap[i][j] == 2)
                q.push(make_pair(i, j));
        }
    }
    
    while(!q.empty()) {
        point = q.front();
        row = point.first;
        col = point.second;
        q.pop();
        
        for(auto &p: dxdy) {
            nextRow = row + p.row;
            nextCol = col + p.col;
            if(tempMap[nextRow][nextCol] == 0
            && 0 <= nextRow && nextRow < numRow
            && 0 <= nextCol && nextCol < numCol) {
                tempMap[nextRow][nextCol] = 2;
                q.push(make_pair(nextRow, nextCol));
            }
        }
    }
    
    int num = 0;
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            if(tempMap[i][j] == 0) num++;
        }
    }
    
    return num;
}

int makeWall(int numWalls) {
    static int answer;
    if(numWalls == 3) {
        
        answer = max(answer, spread());
        return answer;
    }
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            if(map[i][j] == 0) {
                map[i][j] = 1;
                makeWall(numWalls + 1);
                map[i][j] = 0;
            }
        }
    }
    
    return answer;
}

int main() {
    cin >> numRow >> numCol;
    
    for(int i = 0; i < numRow; i++) {
        for(int j = 0; j < numCol; j++) {
            cin >> map[i][j]; 
        }
    }
    
    
    cout << makeWall(0);
    
    
    
    return 0;
}