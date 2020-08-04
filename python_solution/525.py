'''
525. Contiguous Array
Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

'''
# similiar as 325 , treat 0 as -1 , and k is 0
from collections import defaultdict
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_dict = defaultdict(list)
        localsum = maxlen = 0
        for i,val in enumerate(nums):
            if val == 0:
                localsum += -1
            else:
                localsum += val

            if localsum == 0:
                maxlen = i+1
            else:
                if localsum in sum_dict:
                    maxlen = max(maxlen, i-sum_dict[localsum][0])
                    
                else:
                    sum_dict[localsum].append(i)
        return maxlen

foo = Solution()
print(foo.findMaxLength([0,1,0]))

