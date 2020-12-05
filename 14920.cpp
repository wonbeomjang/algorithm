#include <iostream>
using namespace std;

int ans(int c, int i) {
    if (c == 1)
        return i;
    
    if (c % 2 == 0)
        return ans(c / 2, i + 1);
    else
        return ans(3 * c + 1, i + 1);
}

int main() {
    int c;
    
    cin >> c;
    cout << ans(c, 1);
}