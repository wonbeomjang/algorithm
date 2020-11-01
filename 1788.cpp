#include <iostream>
#include <cmath>
#define abs(x) (x > 0 ? x : -x) 
using namespace std;

long long fibo[1000001] = { 0, 1, 1 };

int main() {
    long long n;
    
    for(int i = 3; i < 1000001; i++)
        fibo[i] = fibo[i - 1] + fibo[i - 2];
    
    cin >> n;
    
    if(n > 1L) cout << 1 << endl;
    else if (n == 0L) cout << 0 << endl;
    else cout << -1 << endl;
    
    cout << fibo[abs(n)];
    
    return 0;
    
}

/*

 -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5

*/