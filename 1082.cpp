#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int cost[10];
int totalMoney;
int N;
string maxMoney("");

int main() {
    int temp;
    int index = 0;
    int diff;
    int curDigit;
    
    for(int i = 0; i < 10; i++) cost[i] = -1;
    
    cin >> N;
    
    vector<pair<int, int>> costs(N);
    
    for(int i = 0; i < N; i++) {
        cin >> temp;
        cost[i] = temp;
        costs[i] = {temp, i};
    }
    
    cin >> totalMoney;
    
    sort(costs.begin(), costs.end());
    
    if (costs[0].second == 0) {
        if(costs.size() == 1 || totalMoney < costs[1].first) {
            cout << 0;
            return 0;
        }
    index++;
    }
    
    
    maxMoney.push_back(costs[index].second + '0');
    totalMoney -= costs[index].first;

    while (totalMoney - costs[0].first >= 0)
    {
        maxMoney.push_back(costs[0].second + '0');
        totalMoney -= costs[0].first;
    }
    
    for (int i = 0; i < maxMoney.size(); ++i)
    {
        for (int j = 0; j < 10; ++j)
        {
            if (cost[j] == -1)
                continue;
            
            int curDigit = maxMoney[i] - '0';
            
            int diff = cost[j] - cost[curDigit];
            if (totalMoney - diff >= 0 && curDigit < j)
            {
                totalMoney -= diff;
                maxMoney[i] = char(j + '0');
            }
        }
    }
    
    cout << maxMoney;
}
