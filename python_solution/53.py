class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # by kadane algo O(n)
        maxlocal = maxglobal = float('-inf')
        for i in nums:
            maxlocal = max(maxlocal+i,i)
            maxglobal = max(maxglobal,maxlocal)
        return maxglobal





#[-2,1,-3,4,-1,2,1,-5,4]