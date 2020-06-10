#include<stdio.h>
#include<stdbool.h>
#include<stdint.h>

/**
 * 142. Linked List Cycle II
 * Given a linked list, return the node where the cycle begins. 
 * If there is no cycle, return null
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * 
 * 1,2,3,4,5
     ^	   |
     |------
 */

// determine by length
struct ListNode *detectCycle_bad(struct ListNode *head) {
    int steps = 0 , locallen =0;

    if(!head)
        return NULL;
    
    struct ListNode *cur =head ,*pre =NULL;

    while(cur->next){
        cur=cur->next;
        steps++ ;
        for(pre=head,locallen=0;pre!=cur;pre=pre->next){
            locallen++ ;
        }
        if(locallen < steps)
            return pre ;


    }
    return NULL;
}

//floyd
struct ListNode *detectCycle(struct ListNode *head) {
    int steps = 0 , locallen =0;

    if(!head)
        return false;

    struct ListNode * slow =head , *faster = head;

    while(faster->next && (faster->next->next) ){
        slow = slow ->next;
        faster = faster->next->next;
        if(slow == faster){
            for(faster = head; faster!=slow; faster=faster->next,slow=slow->next)
            ;
            return faster;
        }
    }
    return NULL;
}