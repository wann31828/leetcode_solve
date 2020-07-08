/**No.226
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

struct TreeNode* invertTree(struct TreeNode* root){
    struct TreeNode* tmp ;
    if(!root)
        return ;
    else{
        tmp = root->left;
        root->left = root->right;
        root->right = tmp;
    }
    invertTree(root->left);
    invertTree(root->right);
    return root ;
}