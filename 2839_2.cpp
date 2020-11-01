#include <iostream>
using namespace std;

int main() {
    int num_3kg = 0;
    int num_5kg = 0;
    int total;
    
    cin >> total;
    
    while(total > 0) {
        if(total % 5 == 0) {
            total -= 5;
            num_5kg++;
        }
        else if(total % 3 == 0) {
            total -= 3;
            num_3kg++;
        }
        else if(total > 5) {
            total -= 5;
            num_5kg++;
        }
        else if(total > 3) {
            total -= 5;
            num_3kg++;
        }
        else {
            break;
        }