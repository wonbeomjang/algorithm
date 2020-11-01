#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

constexpr int maxNum = 100000;

int main() {
    int N;
    int start, end, end_before = 0;
    int cnt = 0;
    
    cin >> N;
    vector<pair<int, int>> schedule;
    
    for(int i = 0; i < N; i++) {
        cin >> start >> end;
        schedule.push_back({start, end});
    }
    
    sort(schedule.begin(), schedule.end());
    sort(schedule.begin(), schedule.end(), 
    [](const pair<int, int> &time1, const pair<int, int> &time2) {
        return time1.second < time2.second;
    });
    
    end_before = 0;
    for(auto &p: schedule) {
        start = p.first;
        end = p.second;
        
        if(end_before <= start) {
            cnt++;
            end_before = end;
        }
    }
    
    cout << cnt;
}