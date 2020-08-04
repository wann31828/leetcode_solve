#513. Find Bottom Left Tree Value
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS , level order
class Solution(object):
    def findBottomLeftValue(self,rootnode):
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
            #print (n.value,end=' ')
                if n.left: 
                    nextlevel.append(n.left)
                if n.right: 
                    nextlevel.append(n.right)
            if len(nextlevel) == 0:
                return thislevel[0].val
            #print()
            thislevel = nextlevel