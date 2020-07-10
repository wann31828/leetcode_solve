/*
 232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
*/
#include <stack>
class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    stack<int> s1 , s2;
    /** Push element x to the back of queue. */
    void push(int x) {
        if(s1.empty())
            s1.push(x);
        else
        {
            s2.push(x);
        }
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int rt = s1.top();
        s1.pop();
        if(!s2.empty()){
            while(!s2.empty()){
                s1.push(s2.top());
                s2.pop();
            }
            int tmp = s1.top();
            s1.pop();
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
            s1.push(tmp);
        }
        return rt ;
    }
    
    /** Get the front element. */
    int peek() {
        return s1.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */