'''
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
 and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda s: s[0])
        rst=[]
        left,right=intervals[0][0],intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= right and i[1] > right:        
                right = i[1]
            elif i[0] > right :
                rst.append(list((left,right)))
                left,right=i[0],i[1]
        else:
            rst.append(list((left,right)))
        return rst        