#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> ropes;
    int N, num, ans;
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> num;
        ropes.push_back(num);
    }
    
    sort(ropes.begin(), ropes.end());
    
    ans = 0;
    for(int i = 0; i < N; i++) {
        ans = max(ans, ropes[i] * (N - i));
    }
    
    cout << ans;
    
    return 0;
}