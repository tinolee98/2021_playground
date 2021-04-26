#include<iostream>
#include<string>
#include<cmath>
#include<stack>
#include<typeinfo>
//#include "HW03.h"
using namespace std;

static stack<int> opStack;
static string result;
static char op[] = {'+','*','^',')','(','-','/'}; // index%4 = prior. (+,-)는 0, (*,/)는 1, ^는 2.

// operator라면 op_list에서 알맞은 index를 부여받고, operand라면 7을 return
int findIndex(char _op){
    for(int i=0;i<7;i++){
        if(_op == op[i]){  
            return i;
        }
    }
    return 7;
}

// operand라면 result string에 추가, operator라면 opStack에 push
void inputFunc(char _input){
    int temp;
    temp = findIndex(_input);
    if(temp == 7){
        result += _input;
        cout << "add operand in inputFunc" << endl;
        cout << result << endl;
    }
    else {
        temp = findIndex(_input);
        opStack.push(temp);
        cout << "add opStack in inputFunc" <<opStack.top() << endl;
        cout << "opIndex" <<opStack.top() << endl;
    }
}

void infix2postfix (string _input) {
    // now는 opStack 내의 operation을 꺼내야하는지, 쌓아야하는지 알려주는 boolean marker
    int top;
    int current;
    for(int i=0; i < _input.length(); i++){
        cout << endl << endl<< "result is " << result << " and i is " << i << endl;
        cout << "opStack size is " << opStack.size() << endl;
        top = !opStack.empty() ? opStack.top() : 0;
        cout << "top is " << top << endl;
        current = findIndex(_input[i]);
        cout << "current is " << current << endl;
        if(current == 7){
            inputFunc(_input[i]);
            cout << "add operand" << endl;
        }
        else if(current != 3){
            cout << "input is operator which is not )" << endl;
            if(current%5 >= top%5 || top == 4 || opStack.empty()){
                cout << "input's prior is higher or top is (" << endl;
                inputFunc(_input[i]);  
                continue;
            }
            while(opStack.top() != 4 && !opStack.empty()){
                cout << "top's prior is higher and repeat pop&push" << endl;
                cout << "opStack.size = " <<opStack.size() << endl;
                top = opStack.top();
                opStack.pop();
                result += op[top];
                if(opStack.empty()) break;                
            }
            cout << "pop&push completed" << endl;
            cout<< "result is " << result << endl;
            inputFunc(_input[i]);
        }
        else{
            cout << "input is )" << endl;
            while(top != 4){
                cout << "pop&push to find (" << endl;
                opStack.pop();
                result += op[top];
                top = opStack.top();
            }
            cout << "we found ( and pop it!" << endl;
            opStack.pop();
        }
    }
    while(!opStack.empty()){
        cout << "input string is empty. thus, opStack.empty" << endl;
        top = opStack.top();
        opStack.pop();
        result += op[top];
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

