# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        thislevel = [root]
        rtlist = list()
        while thislevel:
            levelmax = float('-inf')
            nextlevel = list()
            for n in thislevel:
                levelmax = max(levelmax,n.val)
                #print (n.val,end=' ')
                if n.left: 
                    nextlevel.append(n.left)
                if n.right: 
                    nextlevel.append(n.right)
            rtlist.append(levelmax)
            #print()
            thislevel = nextlevel
        return rtlist


