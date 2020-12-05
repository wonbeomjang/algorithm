#include <iostream>
using namespace std;

int main() {
    int T;
    int a, b;
    int ans;
    
    cin >> T;
    
    for(int i = 0; i < T; i++) {
        cin >> a >> b;
        ans = 1;
        for(int i = 0; i < b; i++) {
            ans = (ans * a) % 10;
        }
        
        if (ans) cout << ans << '\n';
        else cout << 10 << '\n';
    }
    
    
}