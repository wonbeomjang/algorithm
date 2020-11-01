#include <iostream>
using namespace std;

constexpr int maxNumTyle = 81;

long long dp[maxNumTyle] = { 0, 4, 6, 10, 16 };

int main() {
    int N;
    
    for(int i = 3; i < maxNumTyle; i++)
        dp[i] = dp[i - 1] + dp[i - 2];
        
    cin >> N;
    
    cout << dp[N];
}