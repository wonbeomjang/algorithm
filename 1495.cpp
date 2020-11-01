#include <iostream>
using namespace std;

constexpr int maxNumMusic = 101;
int volDiff[maxNumMusic];
bool dp[maxNumMusic][1000 + 1];

int main() {
    int numMusic, startVolume, maxVolume;
    bool flag = false;
    
    cin >> numMusic >> startVolume >> maxVolume;
    
    for(int i = 0; i < numMusic; i++) {
        cin >> volDiff[i];
    }
    
    dp[0][startVolume] = true;
    
    for(int i = 1; i <= numMusic; i++) {
        for(int j = 0; j <= maxVolume; j++) {
            if (!dp[i - 1][j]) continue;
            if (j + volDiff[i - 1] <= maxVolume)
                dp[i][j + volDiff[i - 1]] = true;
            if (j - volDiff[i - 1] >= 0)
                dp[i][j - volDiff[i - 1]] = true;
        }
    }
    

    for(int i = maxVolume; i >= 0; i--) {
        if (dp[numMusic][i]) {
            flag = true;
            cout << i;
            break;
        }
    }
    if(!flag) cout << -1;
}