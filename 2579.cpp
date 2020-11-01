#include <iostream>
#include <algorithm>
using namespace std;

constexpr int maxNumStairs = 300 + 1;
int dp[maxNumStairs];
int score[maxNumStairs];

int main() {
    int numStairs;
    cin >> numStairs;
    
    for(int i = 1; i <= numStairs; i++) {
        cin >> score[i];
    }
    
    dp[1] = score[1];
    dp[2] = score[1] + score[2];
    dp[3] = max(score[1] + score[3], score[2] + score[3]);
    
    for(int i = 4; i <= numStairs; i++) {
        dp[i] = score[i] + max(score[i - 1] + dp[i - 3], dp[i - 2]);
    }
    
    cout << dp[numStairs];
}