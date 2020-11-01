#include <iostream>
using namespace std;

constexpr int maxNum = 1001 + 4;
bool dp[maxNum] = {0, 0, 1, 0, 1};

int main() {
    int N;
    
    for(int i = 5; i < maxNum - 4; i++) {
        if(dp[i - 1] && dp[i - 3] && dp[i - 4]) dp[i] = false;
        else dp[i] = true;
    }
    
    cin >> N;
    
    if(dp[N])   cout << "SK";
    else        cout << "CY";
}