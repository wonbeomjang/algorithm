#include <iostream>
#include <cmath>
using namespace std;

constexpr int maxNum = 1001;
int dp[maxNum] = {1, 1, 3, 8};
int inputs[1001];

int main() {
    int P, N, M;
    
    for(int i = 3; i < maxNum; i++) {
        cout << i << endl;
        if ((int)pow(2, i) < maxNum) dp[(int)pow(2, i)] = 3 * powl(2, i - 1);
        if ((int)pow(5, i) < maxNum) dp[(int)pow(5, i)] = 4 * powl(5, i);
        if (2 * (int)pow(5, i) < maxNum )dp[2 * (int)pow(5, i)] = 6 * i;
//        if ((int)pow(10, i) < maxNum)  dp[(int)pow(10, i)] = 15 * pow(10, i - 1);
    }
    
    cin >> P;
    for(int i = 1; i <= P; i++) {
        cin >> N >> M;
        inputs[N] = M;
    }
    
    for(int i = 1; i <= P; i++) {
        cout << i << dp[i];
    }
    
}