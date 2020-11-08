/*
328. Odd Even Linked List
Medium

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
*/
#include<stdio.h>

  struct ListNode {
      int val;
      struct ListNode *next;
  };

struct ListNode* oddEvenList(struct ListNode* head){
    struct ListNode* oddcur, *oddproceed , *evencur , *evenproceed , *evenhead ;
    if(!head)
        return NULL;
    if(! head->next)
        return head;
    /*init*/
    oddcur = head , evencur = head->next ,evenhead = head->next;
    oddproceed = oddcur->next->next ;
    if(oddproceed)
        evenproceed = oddproceed->next;
    
    while(oddproceed){
        oddcur->next = oddproceed;
        oddcur = oddproceed;
        if(oddproceed->next){
            oddproceed = oddproceed->next->next;
        }else
            oddproceed =NULL ;
        
        if(evenproceed){
            evencur->next = evenproceed ;
            evencur = evenproceed;
            if(evenproceed->next){
                evenproceed = evenproceed->next->next;
            }else
                evenproceed =NULL ;
        }
    }
    evencur->next = NULL ;
    oddcur->next = evenhead;
    return head ;
}