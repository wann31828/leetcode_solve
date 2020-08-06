'''
501. Find Mode in Binary Search Tree
Easy

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curcount = maxcount = lastvalue=0
        Modes = []
        stack = []
        cur = root

        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if cur.val == lastvalue:
                    curcount += 1
                else:
                    curcount = 1
                lastvalue = cur.val

                if curcount > maxcount:
                    Modes.clear()  #use del Modes[:] for python 3.2 or lower version
                    Modes.append(cur.val)
                    maxcount = curcount
                elif curcount == maxcount:
                    Modes.append(cur.val)
                cur = cur.right
            else:
                break

        return Modes