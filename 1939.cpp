#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring> //memset
using namespace std;

const int MAX = 100000 + 1;

int num_island;
int num_bridge;
int start, target;

vector<pair<int, int>> edge[MAX];
bool visited[MAX];

bool bfs(int curW) {
    queue<int> q;
    int v;
    int nextV, nextW;
    
    q.push(start);
    visited[start] = true;
    
    while(!q.empty()) {
        v = q.front();
        q.pop();
        
        if (v == target) {
            return true;
        }
        
        for(pair<int, int> &p: edge[v]) {
            nextV = p.first;
            nextW = p.second;
            
            if(!visited[nextV] && curW <= nextW) {
                visited[nextV] = true;
                q.push(nextV);
            }
        }
    }
    
    return false;
}

int main() {
    int from, to, weight;
    int low = 0;
    int hight = 1000000001;
    int mid;
    cin >> num_island >> num_bridge;
    
    for(int i = 0; i < num_bridge; i++) {
        cin >> from >> to >> weight;
        edge[from].push_back({to, weight});
        edge[to].push_back({from, weight});
    }
    
    cin >> start >> target;
    
    while(low <= hight) {
        memset(visited, false, sizeof(visited));
        mid = (low + hight) / 2;
        if (bfs(mid)) {
            low = mid + 1;
        }
        else {
            hight = mid - 1;
        }
        
    }
    
    cout << hight;
    
    return 0;
}
