#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int res;
int N;
int K;
bool visited[26];
vector<string> words;

void learned(int alphabet, int num_learned) {
    if(num_learned == K) {
        int cnt = 0;
        bool flag = true;
        
        for(int i = 0; i < N; i++) {
            flag = true;
            for(int j = 0; j < words[i].length(); j++) {
                if (!(visited[words[i][j] - 'a'])) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cnt++;
            }
        }
        
        res = max(res, cnt);
    }
    else {
        for(int i = alphabet; i < 26; i++) {
            if(!visited[i]) {
                visited[i] = true;
                learned(i, num_learned + 1);
                visited[i] = false;
            }
        }
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    string str;
    
    cin >> N >> K;
    words.resize(N);
    
    for(int i = 0; i < N; i++) {
        cin >> words[i];
        words[i] = words[i].substr(4, words[i].length() - 8);
    }
    
    visited['a' - 'a'] = true;
    visited['c' - 'a'] = true;
    visited['i' - 'a'] = true;
    visited['n' - 'a'] = true;
    visited['t' - 'a'] = true;
    
    if (K < 5) {
        cout << 0;
    }
    else if (K == 26) {
        cout << N;
    }
    else {
        K -= 5;
        learned(0, 0);
        cout << res;
    }
}