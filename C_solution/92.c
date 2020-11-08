/**
 * 92. Reverse Linked List II (Medium)
 *
 *  Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

  struct ListNode {
      int val;
      struct ListNode *next;
  };

struct ListNode* reverseBetween(struct ListNode* head, int m, int n){
    if(!head)
        return NULL;
    if(m==n)
        return head ;
    
    struct ListNode *prev = NULL ,*cur =head ,*proceed = head->next , *p1=NULL , *s1 = NULL ;
    
    for(int i=1 ;i<m;i++){
        p1 = cur ;
        cur = cur->next;
    }
    s1 = cur ;
    proceed = cur->next ;
    //prev = p1 ;

    while( cur && (m++ <= n) ){
        cur ->next = prev;
        prev = cur ;
        cur = proceed ;
        if(cur)
            proceed = cur ->next ;
    }
    if(p1)
        p1->next = prev ;
    s1->next = cur ;

    if(p1)
        return head ;
    else
        return prev ;    
}

