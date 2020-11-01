#include <iostream>
#include <algorithm>
using namespace std;

constexpr int maxNum = 1001;
bool dp[maxNum] = {true, true, false, true};

int main() {
    int N;
    for(int i = 4; i < maxNum; i++) {
        dp[i] = !dp[i - 1]; 
        dp[i] = !dp[i - 3]; 
    }
    
    cin >> N;
    
    if(!dp[N]) cout << "SK";
    else cout << "CY";
}