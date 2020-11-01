#include <iostream>
using namespace std;

constexpr int maxNum = 100000;
int dp[maxNum] = {1, 3};

int main() {
    int N;
    
    for(int i = 2; i <= maxNum; i++)
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901;
    scanf("%d", &N);
    printf("%d",  dp[N]);
}