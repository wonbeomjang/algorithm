#include <iostream>
#include <vector> 
#include <algorithm>
#include <cstring>
using namespace std;

constexpr int maxNumBuildings = 1001;

vector<int> edge[maxNumBuildings];
int cost[maxNumBuildings];
int delay[maxNumBuildings];
bool visited[maxNumBuildings];

int dfs(int builingNum) {
    int maxTime = 0;
    if(visited[builingNum]) return delay[builingNum];
    visited[builingNum] = true;
    
    for(int &adj: edge[builingNum])  {
        if(delay[adj]) maxTime = max(maxTime, delay[adj]);
        else maxTime = max(maxTime, dfs(adj));
    }
    
    delay[builingNum] = maxTime + cost[builingNum];
    
    return delay[builingNum];
}

int main() {
    int numTests;
    int numBuildings;
    int numRules;
    int from, to;
    int targetBuiling;
    
	ios_base::sync_with_stdio(0);
	cin.tie(0);
    
    cin >> numTests;
    
    for(int i = 0; i < numTests; i++) {
        for(auto &vec: edge) vec.clear();
        cin >> numBuildings >> numRules;
        
        for(int i = 1; i <= numBuildings; i++)
            cin >> cost[i];
    
        
        for(int i = 1; i <= numRules; i++) {
            cin >> from >> to;
            edge[to].emplace_back(from);
        }
        
        memset(visited, 0, sizeof(visited));
        memset(delay, 0, sizeof(delay));
        
        cin >> targetBuiling;
        
        cout << dfs(targetBuiling) << '\n';
    }
    
}