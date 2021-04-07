// FastBuffer를 만들어 놓은 header file
// deque를 이용하는 경우 pop(), push(), peek() 등 stack iterator를 사용할 수 없기에
// deque iterators를 사용하였습니다.
#include<iostream>
#include<deque>
using namespace std;

class FastBuffer{
    private:
        deque<char> stack;
        int cursor;


    public:
        FastBuffer() {cursor = 0;}          //instructor
        ~FastBuffer() {}                    //destructor

        int getCursor()
        {
            return cursor;
        }
        
        void setCursor(int _cursor) {cursor = _cursor;}

        void insertLeft(char item)
        {   
            stack.push_front(item);
            //stack.insert(stack.begin() + cursor,item);
            cursor++;
        }

        char deleteLeft()
        {
            int temp = stack[cursor-1];
            //stack.erase(stack.begin() + cursor -1);
            cursor--;
            return temp;
        }

        char deleteRight() 
        {
            int temp = stack[cursor];
            //stack.erase(stack.begin() + cursor);
            cursor--;
            return temp;
        }
        // cursor의 위치를 옮김.
        void moveLeft()
        {
            if (cursor > 0) {
                cursor -= 1;
            }
        }
        void moveRight()
        {
            if (cursor < stack.size()){
                cursor += 1;
            }
        }
        void printBuffer()
        {   
            for(int i=0 ; i < stack.size(); i++){
                cout << stack[i];
            }
            cout << endl;
        }

        // throw에 관련된 (error 관련 함수도 만들어야 함!)
};
