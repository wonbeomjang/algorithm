#include <bits/stdc++.h>
using namespace std;

vector<string> strs;
int n;

int main() {
    cin >> n;
    strs.resize(n);
    string temp("");
    
    for(int i = 0; i < n; i++) {
        cin >> strs[i];
    }
    
    sort(strs.begin(), strs.end(), [](string s1, string s2) -> bool {
        if (s1.length() != s2.length()) return s1.length() < s2.length();
        return s1 < s2;
    });
    
    for(auto &s: strs) {
        if (temp == s) continue;
        cout << s << '\n';
        temp = s;
    }
}