/**
 * 235. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

 

Constraints:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.


Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
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

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if (!root )
        return NULL;
    int miner , bigger ;
    bigger = p->val > q->val ? p->val : q->val ;
    miner = p->val + q->val - bigger ;

    while(1){
        if (!root )
            return NULL;
        if ((miner <= root->val) && (bigger >= root->val))
            return root;
        else if (root->val < miner)
            root = root->right ;
        else 
            root = root ->left ; 
    }
}