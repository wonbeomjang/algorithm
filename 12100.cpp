#include <iostream>
#include <algorithm>
using namespace std;

int board[20][20];
int copy_board[20][20];
int N;
int ans;

void shift(int direction) {
    // 왼쪽
    int index;
    int data;
    if (direction == 0) {
        for(int i = 0; i < N; i++) {
            index = 0;
            for(int j = 0; j < N; j++) {
                if (board[i][j]) {
                    data = board[i][j];
                    board[i][j] = 0;
                    
                    if(board[i][index] == 0) {
                        board[i][index] = data;
                    }
                    else if(board[i][index] == data) {
                        board[i][index] = data * 2;
                        index++;
                    }
                    else {
                        index++;
                        board[i][index] = data;
                    }
                }
            }
        }
    }
    
    else if (direction == 1) {
        for(int i = 0; i < N; i++) {
            index = N - 1;
            for(int j = N - 1; j >= 0; j--) {
                if (board[i][j]) {
                    data = board[i][j];
                    board[i][j] = 0;
                    
                    if(board[i][index] == 0) {
                        board[i][index] = data;
                    }
                    else if(board[i][index] == data) {
                        board[i][index] = data * 2;
                        index--;
                    }
                    else {
                        index--;
                        board[i][index] = data;
                    }
                }
            }
        }
    }
    
    else if (direction == 2) {
        for(int j = 0; j < N; j++) {
            index = 0;
            for(int i = 0; i < N; i++) {
                if (board[i][j]) {
                    data = board[i][j];
                    board[i][j] = 0;
                    
                    if(board[index][j] == 0) {
                        board[index][j] = data;
                    }
                    else if(board[index][j] == data) {
                        board[index][j] = data * 2;
                        index++;
                    }
                    else {
                        index++;
                        board[index][j] = data;
                    }
                }
            }
        }
    }
    
    else if (direction == 3) {
        for(int j = 0; j < N; j++) {
            index = N - 1;
            for(int i = N - 1; i >= 0; i--) {
                if (board[i][j]) {
                    data = board[i][j];
                    board[i][j] = 0;
                    
                    if(board[index][j] == 0) {
                        board[index][j] = data;
                    }
                    else if(board[index][j] == data) {
                        board[index][j] = data * 2;
                        index--;
                    }
                    else {
                        index--;
                        board[index][j] = data;
                    }
                }
            }
        }
    }
}

void dfs(int cnt) {
    if (cnt == N) {
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                ans = max(ans, board[i][j]);
            }
        }
        return;
    }
    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            copy_board[i][j] = board[i][j];
        }
    }
    
    for(int i = 0; i < 4; i++) {
        shift(i);
        dfs(cnt + 1);
        
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                board[i][j] = copy_board[i][j];
            }
        }
    }
    
}

void print_board() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cout << board[i][j] << ' ';
        }
        cout << endl;
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    cin >> N;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }
    dfs(0);
    cout << ans;
}