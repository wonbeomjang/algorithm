#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
using namespace std;

constexpr int maxNumCity = 20 + 1;
constexpr int maxNumTarget = 1000 + 1;

int numCity;
int numTarget;

int dp[maxNumTarget];

int main() {
    int cost, target;
    fill(dp, dp + maxNumTarget, INT_MAX);
    
    cin >> numTarget >> numCity;
    
    dp[0] = 0;
    
    for(int i = 0; i < numCity; i++) {
        cin >> cost >> target;
        
        for(int i = 1; i <= numTarget; i++) {
            if(i < target) {
                dp[i] = min(dp[i], cost);
            }
            else {
                dp[i] = min(dp[i], dp[i - target] + cost);
            }
        }
    }
    
    cout << dp[numTarget];
}