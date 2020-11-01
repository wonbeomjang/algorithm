#include <iostream>
#include <algorithm>
using namespace std;

constexpr int maxNum = 20;
int damage[maxNum];
int pleasure[maxNum];
int maxPleasure[100];

int main() {
    int numPeople;
    
    cin >> numPeople;
    
    for (int i = 0; i < numPeople; i++) cin >> damage[i];
    for (int i = 0; i < numPeople; i++) cin >> pleasure[i];
    
    for(int i = 0; i < numPeople; i++) {
        for(int j = 99; j > 0; j--) {
            if (j - damage[i] > 0) 
                maxPleasure[j] = max(maxPleasure[j], maxPleasure[j - damage[i]] + pleasure[i]);
        }
    }
    
    cout  << maxPleasure[99];
}