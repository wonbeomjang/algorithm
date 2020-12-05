#include <iostream>
#include <vector>
using namespace std;

int numPeople[1000000];
int temp, N;
int B, C;
long long ans;

int main() {
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> temp;
        numPeople[i] = temp;
    }
    
    cin >> B >> C;
    
    for(int i = 0; i < N; i++) {
        numPeople[i] -= B;
        ans++;
        if(numPeople[i] > 0) {
            ans += numPeople[i] / C;
            if (numPeople[i] % C)
                ans++;
        }
    }
    
    cout << ans;
}

//3 2 3 2 3

