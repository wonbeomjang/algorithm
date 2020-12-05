#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string num1, num2;
    int nextDigit = 0;
    string res("");
    string temp("1");
    int n1Size, n2Size;
    char n1, n2;
    char digit;
    int i = 1;
    
    cin >> num1 >> num2;
    
    n1Size = num1.size();
    n2Size = num2.size();
    
    while(i <= n1Size || i <= n2Size) {
        if (i <= n1Size) {
            n1 = num1[n1Size - i] - '0';
        }
        else {
            n1 = 0;
            nextDigit = 0;
        }
        
        if (i <= n2Size) {
            n2 = num2[n2Size - i] - '0';
        }
        else {
            n2 = 0;
            nextDigit = 0;
        }
        
        digit = (n1 + n2 + nextDigit) % 10 + '0';
        nextDigit = (n1 + n2 + nextDigit) / 10;
        res.insert(0, 1, digit);
        i++;
    }
    
    if (nextDigit)
        res.insert(0, temp);
    
    cout << res;
}