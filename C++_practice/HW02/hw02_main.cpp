// FastBuffer를 테스트하는 main code
#include<iostream>
#include "buffer.h"
using namespace std;

int main()
{
    FastBuffer myBuff;

    cout << "Cursor at " << myBuff.getCursor() << "\n";
    myBuff.insertLeft('1');
    cout << "Cursor at " << myBuff.getCursor() << "\n";
    myBuff.insertLeft('2');
    myBuff.insertLeft('3');
    myBuff.insertLeft('4');
    myBuff.setCursor(3);
    myBuff.insertLeft('5');
    myBuff.insertLeft('6');
    myBuff.insertLeft('7');
    cout << "Cursor at " << myBuff.getCursor() << "\n";

    //Print Buffer:
    myBuff.printBuffer();

    //Add "*$" at position 6
    myBuff.setCursor(6);
    myBuff.insertLeft('*');
    myBuff.insertLeft('$');

    myBuff.printBuffer();

    //delete the junk characters
    cout << "Deleted: " << myBuff.deleteLeft() << "\n";
    cout << "Deleted: " << myBuff.deleteLeft() << "\n";
    
    myBuff.printBuffer();
    return 0;
}