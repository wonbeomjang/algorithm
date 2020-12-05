#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, w, ans = 0;
    vector<int> ropes;
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> w;
        ropes.push_back(w);
    }
    
    sort(ropes.begin(), ropes.end());
    
    for(int i = 0; i < N; i++)
        ans = max(ans, ropes[i] * (N - i));
    cout << ans;
}