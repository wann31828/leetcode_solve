'''
209. Minimum Size Subarray Sum
Medium

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''
#sliding window
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        win_srt , win_end  = 0,0
        min_win_size = float('inf')
        cur_win_sum = 0
        for i in nums:
            cur_win_sum += i
            while(cur_win_sum >= s):
                min_win_size = min(min_win_size,win_end-win_srt+1)
                cur_win_sum -= nums[win_srt]
                win_srt += 1

            win_end += 1
        return 0 if min_win_size == float('inf') else min_win_size 

#a = Solution()
#print(a.minSubArrayLen(7,[2,3,1,2,4,3]))