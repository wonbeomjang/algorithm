#include <iostream>
using namespace std;
constexpr int MAXNUM = 31;

int main() {
    int dp[MAXNUM][MAXNUM] = {{1}, {1, 1}};
    int num1, num2, temp;
    int numTest;;
    
    for(int i = 2; i < MAXNUM; i++) {
        dp[i][0] = 1;
        dp[i][i] = 1;
        for(int j = 1; j < i; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
        }
    }
    
    cin >> numTest;
    
    for(int i = 0; i < numTest; i++) {
        cin >> num1 >> num2;
        
        if (num1 < num2) {
            temp = num1;
            num1 = num2;
            num2 = temp;
        }
        
        cout << dp[num1][num2] << endl;
    }
    
    
    return 0;
}