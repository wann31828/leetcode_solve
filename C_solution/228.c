/**
 * 228. Given a complete binary tree, count the number of nodes.
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

int countNodes(struct TreeNode* root){
    if(!root)
        return 0;
    else{
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
}
