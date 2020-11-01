#include <iostream>
using namespace std;

constexpr int maxNum = 46;
long long dp[maxNum] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597};

int main() {
    int N;
    
    for(int i = 18; i < maxNum; i++)
        dp[i] = dp[i - 1] + dp[i - 2];
    
    cin >> N;    
    cout << dp[N];
}