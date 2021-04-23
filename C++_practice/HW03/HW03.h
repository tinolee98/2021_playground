// HW03.h
#include<iostream>
#include<string>
using namespace std;

void input (string _input) {
    for(int i=0; i < _input.length(); i++){
        if(isdigit(_input[i])){
            nStack.push(_input[i]);
            cout << nStack.top() <<endl;
        }
        else {
            opStack.push(_input[i]);
            cout << opStack.top() << endl;
        }
    }
}