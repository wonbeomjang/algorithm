#include <iostream>
using namespace std;

constexpr int MAXNUM = 12;

int dp[MAXNUM] = {0, 1, 2, 4, 7};

int main() {
    int numTest;
    int num;
    
    for(int i = 4; i < MAXNUM; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    
    cin >> numTest;
    
    for(int i = 0; i < numTest; i++) {
        cin >> num;
        cout << dp[num] << endl;
    }
    
    return 0;
}