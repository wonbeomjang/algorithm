#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> ports;

int main() {
    int n;
    int port;
    
    cin >> n;
    ports.push_back(0);
    for(int i = 1; i <= n; i++) {
        cin >> port;
        
        if (port > ports.back()) {
            ports.push_back(port);
        }
        else {
            auto position = lower_bound(ports.begin(), ports.end(), port);
            *position = port;
        }
    }
    
    cout << ports.size() - 1;
    
}