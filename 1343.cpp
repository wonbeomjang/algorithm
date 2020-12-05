#include <iostream>
#include <string>
using namespace std;

int main() {
    string poly;
    int pos;
    
    cin >> poly;
    
    while(pos = poly.find("XXXX"), pos != string::npos) 
        poly.replace(pos, 4, "AAAA");
    
    while(pos = poly.find("XX"), pos != string::npos) 
        poly.replace(pos, 2, "BB");

    
    if(poly.find("X") == string::npos)
        cout << poly;
    else
        cout << -1;
}