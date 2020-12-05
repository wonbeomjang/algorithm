#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int N;
int maxNum = INT_MIN;
int minNum = INT_MAX;
int nums[11];

void dfs(int numPlus, int numMinus, int numTimes, int numDiv, int cnt, int res) {
    if (cnt == N) {
        maxNum = max(maxNum, res);
        minNum = min(minNum, res);
        return;
    }
    if  (numPlus) dfs(numPlus - 1, numMinus, numTimes, numDiv, cnt + 1, res + nums[cnt]);
    if (numMinus) dfs(numPlus, numMinus - 1, numTimes, numDiv, cnt + 1, res - nums[cnt]);
    if (numTimes) dfs(numPlus, numMinus, numTimes - 1, numDiv, cnt + 1, res * nums[cnt]);
    if   (numDiv) dfs(numPlus, numMinus, numTimes, numDiv - 1, cnt + 1, res / nums[cnt]);
}

int main() {
    int temp;
    int numPlus, numMinus, numTimes, numDiv;
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> nums[i];
    }
    
    cin >> numPlus >> numMinus >> numTimes >> numDiv;
    
    dfs(numPlus, numMinus, numTimes, numDiv, 1, nums[0]);
    
    cout << maxNum << endl << minNum;
}