#include <iostream>

using namespace std;

int main(){
    long long a, b, c;
    long long min, max; 

    cin >> a >> b >> c;

    if ((a >= b) && (a >= c)){
        max = a;
        if (b <= c){
            min = b;
        }
        else{
            min = c;
        }
    }
    else if ((b >= c) && (b >= a)){
        max = b;
        if (a <= c){
            min = a;
        }
        else{
            min = c;
        }
    }
    else if ((c >= a) && (c >= b)){
        max = c;
        if (a <= b){
            min = a;
        } 
        else{
            min = b;
        }
    }

    cout << min << " " << max;
    return 0;
}