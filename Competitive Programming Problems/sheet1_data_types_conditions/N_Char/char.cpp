#include <iostream>

using namespace std;

int main(){
    char c;
    cin >> c;

    int ascii_c = c;
    if (ascii_c >= 65 && ascii_c <= 90){
        char c_tmp = ascii_c + 32;
        cout << c_tmp << endl;
    } 
    else if (ascii_c >= 97 && ascii_c <= 122){
        char c_tmp = ascii_c - 32;
        cout << c_tmp << endl;
    }
    
    return 0;
}