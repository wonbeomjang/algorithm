#include <iostream>
using namespace std;

constexpr int MAXVAL = 10001;
constexpr int MAXNUMCOIN = 1000;
int dp[MAXNUM];
int coin[MAXNUMCOIN];

int main() {
    int n, k;
    
    for(int i = 0; i < n; i++) {
        cin >> coin[i];
        dp[coin[i]] = 1;
    }
    
    for(int i = 1; i <= k; i++) {
        dp[i] = 
    }
    
    return 0;
}