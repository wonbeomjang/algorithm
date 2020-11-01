#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;


int dp[100000];
int numItem;


int main() {
    int weight, value, maxWeight;
    cin >> numItem >> maxWeight;
    
    dp[0] = 0;
    
    for(int i = 0; i < numItem; i++) {
        cin >> weight >> value;
        for(int i = maxWeight; i > 0; i--) {
            if (i - weight >= 0)
                dp[i] = max(dp[i], dp[i - weight] + value);
        }
    }
    
    cout << dp[maxWeight];
}