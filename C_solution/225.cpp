/* 225. Implement Stack using Queues
 Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

*/
#include <queue>
#include <iostream>
using namespace std;
class MyStack {
public:
    queue<int> q1 ,q2;
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        if(!q1.empty())
            q1.push(x);
        else
        {
            q2.push(x);
        }
                
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int val = 0 ,size = 0 , i=0;
        if(!q1.empty()){
            if(q1.size()==1){
                val = q1.back();
                q1.pop();
            }else{
                size = q1.size() ;
                for(i=1; i<size;i++){
                    val = q1.back();
                    q2.push(q1.front());
                    q1.pop();
                }
                q1.pop();
            }
        }else if(!q2.empty()){
                if(q2.size()==1){
                val = q2.back();
                q2.pop();
            }else{
                size = q2.size() ;
                for(i=1; i<size;i++){
                    val = q2.back();
                    q1.push(q2.front());
                    q2.pop();
                }
                q2.pop();
            }
        }
        return val ;
    }
    
    /** Get the top element. */
    int top() {
        if(!q1.empty())
            return q1.back();
        else if(!q2.empty())
            return q2.back();
        else
        {
            return 0;
        }
        
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */