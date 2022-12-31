#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    cout << fixed << setprecision(9);
    double rad;
    double pi = 3.141592653; 
    cin >> rad;
    cout << (pi*rad*rad);
    return 0;   
}