#include <iostream>
using namespace std;

pair<int, int> dp[46] = { {1, 0} };

int main() {
    int k;

    for(int i = 1; i < 46; i++)
        dp[i] = {dp[i - 1].second, dp[i - 1].first + dp[i - 1].second};
        
    cin >> k;
        
    cout << dp[k].first << ' ' << dp[k].second;
}