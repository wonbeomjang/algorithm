#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string seat;

int main() {
    int index = 0;
    int cnt = 1;
    int N;
    cin >> N;
    cin >> seat;
    
    while(index < seat.size()) {
        if(seat[index] == 'S') cnt++, index++;
        else {
            cnt++;
            index += 2;
        }
    }
    
    cout << min(cnt, N);

    
}