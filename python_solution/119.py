'''
119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur = [1,1]
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return cur
        else:
            for i in range(2,rowIndex+1):
                pre = cur[:]
                #cur = []
                for j in range(i+1):
                    #i[n] = i-1[n-1] + i-1[n]
                    if j == 0:
                        cur[j] =1
                    elif j == i:
                        cur.append(1)
                    else:
                        cur[j] = pre[j-1] + pre[j]
        #print(cur)
        return cur

