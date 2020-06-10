#include<stdio.h>
#include<stdbool.h>
#include<stdint.h>

/* 
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3


*/

  struct ListNode {
      int val;
      struct ListNode *next;
  };

struct ListNode* deleteDuplicates(struct ListNode* head){
    if(!head)
        return NULL;
    if(!head->next)
        return head ;
    
    struct ListNode* pre=head , *cur=head ;

    while(cur->next){
        while(cur->next && (cur->next->val == cur->val))
            cur = cur->next ;
        
        if(cur->next){
            pre->next = cur->next;
            cur = cur->next;
            pre = cur;

        }else{
            pre->next = NULL;
            return head;
        }
    }
    return head ;
}