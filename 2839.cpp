#include <iostream>
#include <algorithm>
using namespace std;

constexpr int maxNum = 5001;

int dp[maxNum];

int main() {
    int N;
    
    for(int i = 1; i < maxNum; i++) {
        if(i % 3 == 0) dp[i] = i / 3;
        if(i % 5 == 0) dp[i] = i / 5;
        if(i > 3 && dp[i - 3]) dp[i] = dp[i - 3] + 1;
        if(i > 5 && dp[i - 5]) dp[i] = dp[i - 5] + 1;
    }
    cin >> N;
    
    if(!dp[N])  cout << -1;
    else        cout << dp[N];
}