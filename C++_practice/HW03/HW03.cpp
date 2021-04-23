#include<iostream>
#include<string>
#include<cmath>
#include<stack>
#include<typeinfo>
//#include "HW03.h"
using namespace std;

static stack<char> nStack;
static stack<int> opStack;
static string result;
static char op[] = {'+','*','^',')','(','-','/'}; // index%4 = prior. (+,-)는 0, (*,/)는 1, ^는 2.

int findIndex(char _op){
    for(int i=0;i<7;i++){
        if(_op == op[i])
            return i;
    }
    return 7;
}

void inputFunc(char _input){
    int temp;
    temp = findIndex(_input);
    if(temp == 7){
        result += _input;
        cout << result << endl;
    }
    else {
        temp = findIndex(_input);
        opStack.push(temp);
        cout << "opIndex" <<opStack.top() << endl;
    }
}

void infix2postfix (string _input) {
    bool now = 0;
    int temp;
    int current;
    for(int i=0; i < _input.length(); i++){
        if(isdigit(_input[i])){ // input이 숫자라면
            inputFunc(_input[i]);
        }
        else{
            cout << "I'm here! and now is " << now << endl;
            current = findIndex(_input[i]);
            if(!opStack.empty() && current%5 < opStack.top()%5 && opStack.top() != 4){
                now = 1;
            }
            if(_input[i] == ')' || now){
                while (opStack.top() != 4 && !opStack.empty()){
                    temp = opStack.top();
                    opStack.pop();
                    cout << "op" <<op[temp] << endl;
                    result += op[temp];
                    cout << result << endl;
                }
                if (!opStack.empty()) opStack.pop();
                now = 0;
                inputFunc(_input[i]);
            }
            else{ // input이 op인 경우
                inputFunc(_input[i]);
            }
        }
    }
    while(!opStack.empty()){
        temp = opStack.top();
        opStack.pop();
        result += temp;
        cout << temp <<result << endl;
    }
}

// infix -> postfix
int main(){
    string input;
    cin >> input;
    infix2postfix(input);
    cout << result << endl;
    int x;
    return 0;
}

