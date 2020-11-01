#include <iostream>
#include <vector>
#define MAXSIZE 101
using namespace std;

vector<int> edge[MAXSIZE];
bool computer[MAXSIZE];
int numComputer;
int numEdge;

int infect(int num) {
    int static numInfected = 0;
    computer[num] = true;
    
    for(auto &n: edge[num]) {
        if (!computer[n]) {
            numInfected++;
            infect(n);
        }
    }
    
    return numInfected;
}

int main() {
    int from, to;
    int ans = 0;
    cin >> numComputer;
    cin >> numEdge;
    
    for(int i = 0; i < numEdge; i++) {
        cin >> from >> to;
        edge[from].push_back(to);
        edge[to].push_back(from);
    }
    
    computer[1] = true;
    
    
    cout << infect(1);
}