#include <stdbool.h>
/**
 * 100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

  struct TreeNode {
      int val;
      struct TreeNode *left;
      struct TreeNode *right;
  };

bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if (!p && !q)
        return true;
    else if((!p && q) || (p && !q))
        return false;
    else if (p->val != q->val)
        return false;
    return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
}