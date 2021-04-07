// FastBuffer를 만들어 놓은 header file
// 2개의 deque를 이용하여 stack을 구현하였으며,
// insertLeft, deleteLeft, deleteRight, moveRight, moveLeft는 모두 O(1) 입니다.
// push_front(), pop_front(), subscript[0]과 size()만 사용하였습니다.
// error가 발생하는 경우 error message와 함께 exit()를 이용하여 강제 종료하였습니다.
#include<iostream>
#include<deque>
using namespace std;

class FastBuffer{
    private:
        deque<char> front;
        deque<char> back;
        int cursor;

    public:
        FastBuffer() {cursor = 0;}          //instructor
        ~FastBuffer() {}                    //destructor

        int getCursor()
        {
            return cursor;
        }
        
        void setCursor(int _cursor)
        {
            int temp;
            cursor = _cursor;
            int size = front.size();
            if (cursor > front.size() + back.size()){
                cout << "fail to set cursor!" << endl;
                exit(1);
            }
            if (front.size()+1 > cursor){
                for(int i=0;i<size+1-cursor;i++){
                    temp = front[0];
                    front.pop_front();
                    back.push_front(temp);
                }
            }
            else if (front.size()+1 < cursor){
                for(int i=0;i<front.size()+1-cursor;i++){
                    temp = back[0];
                    back.pop_front();
                    front.push_front(temp);
                }
            }
        }

        void insertLeft(char item)
        {   
            int temp;
            if (cursor > 0){
                temp = back[0];
                back.pop_front();
                front.push_front(temp);
                back.push_front(item);
            }
            else{
                back.push_front(item);
            }
            cursor++;
        }

        char deleteLeft()
        {
            if(cursor <= 0){
                cout << "fail to delete!" << endl;
                exit(1);
            }
            cursor--;
            int result = back[0];
            back.pop_front();
            int temp = front[0];
            front.pop_front();
            back.push_front(temp);
            return result;
        }

        char deleteRight() 
        {
            if(cursor >= back.size() + front.size()){
                cout << "fail to delete!" << endl;
                exit(1);
            }
            int temp = back[0];
            back.pop_front();
            int result = back[0];
            back.pop_front();
            back.push_front(temp);
            return result;
        }

        // cursor의 위치를 옮김.
        void moveLeft()
        {
            if (cursor > 0) {
                cursor--;
                int temp = front[0];
                front.pop_front();
                back.push_front(temp);
            }
            else{
                cout << "fail to move cursor!" << endl;
                exit(1);
            }
        }
        void moveRight()
        {
            if (cursor < front.size() + back.size()) {
                cursor++;
                int temp = back[0];
                back.pop_front();
                front.push_front(temp);
            }
            else{
                cout << "fail to move cursor!" << endl;
                exit(1);
            }
        }
        void printBuffer()
        {   
            int i;
            // 밑의 주석을 제거하면 front, back deque가 작동하는 구조를 볼 수 있습니다.
            /*for(i=0; i<front.size(); i++){
                cout << front[i];
            }
            cout << ' ';
            for(i=0 ; i < back.size(); i++){
                cout << back[i];
            }*/
            for(i=front.size()-1; i>=0; i--){
                cout << front[i];
            }
            for(i=0 ; i < back.size(); i++){
                cout << back[i];
            }
            cout << endl;
        }
};
