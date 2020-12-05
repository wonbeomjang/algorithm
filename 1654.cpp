#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K;
long long len;
vector<long long> ropes;
long long maxLen;

long long getLength(long long min, long long max) {
    long long mid;
    long long res;
    
    while(min <= max) {
        res = 0;
        mid = (min + max) / 2;
        // mid로 만들 수 있는 줄 갯수
        for (long long len: ropes) {
            res += len / mid;
        }
        
        if (N <= res) {
            min = mid + 1;
        }
        else {
            max = mid - 1;
        }
    }
    
    
    return max;
}

int main() {
    cin >> K >> N;
    
    for(int i = 0; i < K; i++) {
        cin >> len;
        ropes.push_back(len);
    }
    
    cout << getLength(1, INT32_MAX);
}