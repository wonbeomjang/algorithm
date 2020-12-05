#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool errors[20];

bool check(int num) {
    
    if (num == 0)
        return errors[0] ? false: true;
    
    while(num > 0) {
        if (errors[num % 10])
            return false;
        num /= 10;
    }
    
    return true;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int targetNum;
    int numErrors;
    int minimum = 600001;
    int temp;
    
    cin >> targetNum;
    cin >> numErrors;
    
    for (int i = 0; i < numErrors; i++) {
        cin >> temp;
        errors[temp] = true;
    }
    
    for(int i = 0; i < 1000000; i++) {
        if (check(i))
            minimum = min(minimum, (int)to_string(i).length() + abs(targetNum - i));
        if (i == 100)
            minimum = min(minimum, + abs(targetNum - i));
    }
    
    cout << minimum;
}

