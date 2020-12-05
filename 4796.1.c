#include <stdio.h>

int main() {
    int L, P, V;
    int numCases = 0;
    
    while(scanf("%d %d %d", &L, &P, &V), numCases++, L || P || V) {
        printf("Case %d: %d", numCases, (V / P) * L + ((V % P) > L ? L : V % P));
    }
    
    return 0;
}