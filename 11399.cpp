#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int numPeople;
    vector<int> durations;
    int d;
    int ans = 0;
    
    cin >> numPeople;
    
    for(int i = 0; i < numPeople; i++) {
        cin >> d;
        durations.push_back(d);
    }
    
    sort(durations.begin(), durations.end(), [](int n1, int n2) -> bool {
        return n1 > n2;
    });
    
    
    for(int i = 1; i <= durations.size(); i++) {
        ans += i * durations[i - 1];
    }
    cout << ans;
}