'''
506. Relative Ranks
Easy

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:

    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rt_list = list()
        nums_sort = sorted(nums,reverse=True)
        for i in nums:
            rank = nums_sort.index(i)
            if rank >= 3:
                rt_list.append(str(rank+1))
            elif rank == 2 :
                rt_list.append("Bronze Medal")
            elif rank == 1:
                rt_list.append("Silver Medal")
            elif rank == 0:
                rt_list.append("Gold Medal")
        return rt_list

