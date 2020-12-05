#include <iostream>
#include <string>
using namespace std;

int main() {
    string nums;
    int numFlipx2 = 0;
    
    cin >> nums;
    
    for(int i = 0; i < nums.length() - 1; i++) {
        if(nums[i] != nums[i + 1]) numFlipx2++;
    }
    
    cout << (numFlipx2 + 1) / 2;
}

// 000111001100111000