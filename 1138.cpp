#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

constexpr int maxNumPeople = 10;
int tallerThan[maxNumPeople];
int queue[maxNumPeople];

int main() {
    int numPeople;
    int numZeros;
    
    cin >> numPeople;
    
    for(int i = 0; i < numPeople; i++) {
        cin >> tallerThan[i];
    }
    
    
    for(int i = 0; i < numPeople; i++) {
        numZeros = 0;
        for(int j = 0; j < numPeople; j++) {
            if (numZeros == tallerThan[i] && !queue[j]) {
                queue[j] = i + 1;
                break;
            }
            else if(queue[j] == 0) {
                numZeros++;
            }
        }
    }
    
    for(int i = 0; i < numPeople; i++) {
        cout << queue[i] << ' ';
    }
    
    
    return 0;
}