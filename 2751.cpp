#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, temp;
    vector<int> nums;
    
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> temp;
        nums.push_back(temp);
    }
    
    sort(nums.begin(), nums.end());
    
    for (int n: nums)
        cout << n << '\n';
}