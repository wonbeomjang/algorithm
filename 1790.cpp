#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> nums;
vector<int> finds;

int main() {
    int N, M;
    int temp;
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> temp;
        nums.push_back(temp);
    }
    
    cin >> M;
    
    for(int i = 0; i < M; i++) {
        cin >> temp;
        finds.push_back(temp);
    }
    
    for(int n: nums) {
        cout << n << ' ' << binary_search(nums.begin(), nums.begin() + N, n) << endl;
    }
}