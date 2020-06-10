#include<stdio.h>
#include<stdbool.h>
#include<stdint.h>

/**
 * 141. Linked List Cycle
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/*Floyd Cycle Detection algorithm */
bool hasCycle(struct ListNode *head) {

    if(!head)
        return false;

    struct ListNode * slow =head , *faster = head;

    while(faster->next && (faster->next->next) ){
        slow = slow ->next;
        faster = faster->next->next;
        if(slow == faster)
            return true;
    }
    return false;
    
}