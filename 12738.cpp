#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

vector<int> nums;
vector<int> LIS;

int main() {
    int N;
    
    cin >> N;
    nums.resize(N);
    
    LIS.push_back(INT_MIN);
    
    for(int i = 0; i < N; i++) {
        cin >> nums[i];
    }
    
    for(int n: nums) {
        if(LIS.back() < n) {
            LIS.push_back(n);
        }
        else {
            auto iter = lower_bound(LIS.begin(), LIS.end(), n);
            *iter = n;
        }
    }
    
    cout << LIS.size() - 1;
}