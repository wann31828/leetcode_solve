/**
206
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    typedef struct ListNode Node;
    Node *pre ,*cur ,*preced ;
    if (!head)
        return NULL;
    pre = NULL , cur =head , preced = cur->next;
    while (preced)
    {
        cur->next = pre;
        pre = cur ;
        cur = preced ;
        preced = preced->next;
    }
    cur->next = pre;
    return cur;
}