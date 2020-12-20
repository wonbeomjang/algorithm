#include <iostream>
#include <vector>
#include <climits>
using namespace std;


int main() {
    int n, cnt = 1;
    vector<int> arr;
    
    cin >> n;
    arr.resize(n + 1);
    
    for(int i = 1; i <= n; i++) {
        cin >> arr[i];
        if (arr[i - 1] > arr[i])
            cnt++;
    }
    
    cout << cnt;
}
