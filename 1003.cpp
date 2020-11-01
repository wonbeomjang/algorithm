#include <iostream>
using namespace std;

constexpr int MAXNUM = 41;

int main() {
    int numTest, num;
    pair<int, int> dp[MAXNUM] = {{1, 0}, {0, 1}, {1, 1}, {1, 2}};
    
    for(int i = 4; i < MAXNUM; i++) {
        dp[i] = {dp[i - 1].first + dp[i - 2].first, dp[i - 1].second + dp[i - 2].second};
    }
    
    cin >> numTest;
    
    for(int i = 0; i < numTest; i++) {
        cin >> num;
        cout << dp[num].first << ' ' << dp[num].second << endl;
    }
    
    return 0;
} 