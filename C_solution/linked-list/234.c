#include<stdbool.h>
/**
234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
 */

  struct ListNode {
      int val;
      struct ListNode *next;
  };

bool isPalindrome(struct ListNode* head){
    if(!head || !head->next)
        return true;
    
    struct ListNode* cur =head ,*str =head;
    int i ,j;
    for(i=1;cur->next;i++)
        cur=cur->next;
    cur = head;
    int arr[i] ;

    for(j = 0;j<i ;j++){
        arr[j] = cur->val;
        cur = cur->next ;
    }
    for(i=0,j=sizeof(arr)/sizeof(int)-1 ;i<j;i++ , j--){
        if(arr[i] != arr[j])
            return false;
    }
    return true;
}