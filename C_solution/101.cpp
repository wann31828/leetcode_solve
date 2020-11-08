/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

/*
class Solution {
public:
    bool isOpposite(TreeNode* left,TreeNode* right)
    {
        if(!left && !right) return true;
        
        if(!left && right) return false;
        
        if(left && !right) return false;
        
        if(left->val != right->val) return false;
        
        return isOpposite(left->left,right->right) && isOpposite(left->right,right->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return isOpposite(root->left,root->right);
    }
};
*/

class Solution {
public:
    bool isOpposite(TreeNode* left,TreeNode* right){
        if ( !(left || right))  return true;

        if (!left != !right) return false;

        if (left->val != right ->val) return false;

        return (isOpposite(left->left,right->right) && isOpposite(left->right,right->left)) ;
    }
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return isOpposite(root->left,root->right);
    }
};