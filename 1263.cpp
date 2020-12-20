#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> schedule;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    int T, S;
    int endTime;
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> T >> S;
        schedule.push_back({T, S});
    }
    
    sort(schedule.begin(), schedule.end(), 
        [](pair<int, int> p1, pair<int, int> p2) -> bool {
        return p1.second > p2.second;
    });
    
    for(int i = 1; i < schedule.size(); i++) {
        endTime = schedule[i - 1].second - schedule[i - 1].first;
        
        if(endTime < schedule[i].second) {
            schedule[i].second = endTime;
        }
    }
    
    endTime = schedule[N - 1].second - schedule[N - 1].first;
    if (endTime < 0)
        cout << -1;
    else
        cout << endTime;
}