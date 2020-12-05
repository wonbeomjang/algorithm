#include <iostream>
using namespace std;

int main() {
    int L, P, V;
    int ans;
    int numCases = 0;
    
    while(cin >> L >> P >> V, numCases++, L || P || V) {
        ans = (V / P) * L + ((V % P) > L ? L : V % P);
        cout << "Case " << numCases << ": " << ans << endl;
    }
    
}