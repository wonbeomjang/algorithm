#include <iostream>
#include <string>
using namespace std;

int main() {
    string strs[50];
    char res[50] = { 0 };
    char c;
    int N;
    bool flag;
    
    cin >> N;
    
    for(int i = 0; i < N; i++)
        cin >> strs[i];
        
    
    for(int i = 0; i < strs[0].length(); i++) {
        c = strs[0][i];
        flag = false;
        for(int j = 1; j < N; j++) {
            if (c != strs[j][i]) {
                flag = true;
            }
        }
        
        if (flag) {
            res[i] = '?';
        }
        else {
            res[i] = c;
        }
    }
    
    cout << res;
}