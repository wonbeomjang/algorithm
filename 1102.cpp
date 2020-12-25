#include <bits/stdc++.h>
constexpr int inf = 987654321;
using namespace std;

int cost[17][17];
bool on[17];
int dp[100000];
int P;
int N;
int state;

int dfs(int cnt) {
    if(cnt == P) {
        return 0;
    }
    
    int &cur_cost = dp[state];
    if(cur_cost != -1)
        return cur_cost;
    
    cur_cost = inf;
    
    for(int i = 0; i < N; i++) {
        // i가 안켜져있으면
        if (!((1 << i) & state)) {
            for(int j = 0; j < N; j++) {
                if(i == j)
                    continue;
                // j가 켜져있으면
                if((1 << j) & state) {
                    state |= (1 << i);
                    cur_cost = min(cur_cost, dfs(cnt + 1) + cost[j][i]);
                    state ^= (1 << i);
                }
            }
        }
    }
    
    return cur_cost;
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    memset(dp, -1, sizeof(dp));
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> cost[i][j];
        }
    }
    
    string str;
    
    cin >> str;
    cin >> P;
    
    for(int i = 0; i < N; i++) {
        if(str[i] == 'Y') {
            P--;
            state |= (1 << i);
        }
    }
    
    int ans = dfs(0);
    
    if (P <= 0)
        cout << 0;
    else if (ans == inf) 
        cout << -1;
    else
        cout << ans;
}