#include <iostream>
#include <algorithm>
using namespace std;

constexpr int maxLen = 1001;

int dp[maxLen][maxLen];
char map[maxLen][maxLen];
int numRow, numCol;

int main() {
    cin >> numRow >> numCol;
    int num;
    int maxNum = 0;
    
    for(int i = 1; i <= numRow; i++) {
        for(int j = 1; j <= numCol; j++) {
            cin >> map[i][j];
            map[i][j] -= '0';
            dp[i][j] = map[i][j];
            if(map[i][j]) maxNum = 1;
        }
    }
    
    
    for(int i = 1; i <= numRow; i++) {
        for(int j = 1; j <= numCol; j++) {
            if(dp[i][j] && dp[i - 1][j - 1] && dp[i - 1][j] && dp[i][j - 1]) {
                dp[i][j] = min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]}) + 1;
                maxNum = max(dp[i][j], maxNum);
            }
        }
    }
    
    
    
    cout << maxNum * maxNum;
}

/*
 011100
 011111
 011111
 011111
 
 011100
 012211
 012322
 012333
*/