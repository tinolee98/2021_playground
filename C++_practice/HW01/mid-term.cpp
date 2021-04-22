#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include "mid-term.h"
using namespace std;

int sum_f(int n){
    if (n == 0)
        {return n;}
    else{
        return n + sum_f(n-1);
    }
}
int main(){
    int sum = 0;
    int n = 5;
    int result = sum_f(n);
    cout<< result <<endl;
}
