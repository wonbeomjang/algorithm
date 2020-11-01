#include <iostream>
using namespace std;

int coin[] = { 500, 100, 50, 10, 5, 1 };

int main() {
    int remain = 1000;
    int given = 0;
    int numCoin = 0, n = 0;
    
    cin >> given;
    remain -= given;
    
    for(int &val: coin) {
        n = remain / val;
        remain -= val * n;
        numCoin += n;
    }
    
    cout << numCoin;
}