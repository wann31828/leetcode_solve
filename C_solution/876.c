/* 
876. Middle of the Linked List
Easy

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include<stdlib.h>

  struct ListNode {
      int val;
      struct ListNode *next;
  };

// fast slow pointer
struct ListNode* middleNode(struct ListNode* head){
    if(!head)
        return NULL ;
    else if(!head->next)
        return head;

    struct ListNode *slow_p = head, *fast_p =head->next;
    while(1){
        if( !(fast_p->next) || !(fast_p->next->next))
            return slow_p->next;
        else{
            slow_p = slow_p->next;
            fast_p = fast_p->next->next;
        }
    }
}