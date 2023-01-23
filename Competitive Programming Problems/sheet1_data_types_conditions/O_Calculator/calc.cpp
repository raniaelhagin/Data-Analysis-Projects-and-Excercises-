#include <iostream>

using namespace std; 

int main(){
    int pre_op, post_op;
    char op; 

    cin >> pre_op >> op >> post_op;

    if (op == '+'){
        cout << pre_op + post_op;
    }
    else if (op == '-'){
        cout << pre_op - post_op;
    }
    else if (op == '*'){
        cout << pre_op * post_op;
    }
    else{
        cout << pre_op / post_op;
    }
    return 0;
}