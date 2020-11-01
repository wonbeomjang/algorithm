#include <iostream>
using namespace std;

constexpr int MAXNUM = 91;

int main() {
    long long dp[MAXNUM] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597};
    int num;
    
    cin >> num;
    
    for(int i = 18; i < MAXNUM; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    cout << dp[num];
}