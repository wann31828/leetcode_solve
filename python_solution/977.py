'''
977. Squares of a Sorted Array
Easy

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.

'''
# two pointer
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p1 , p2 = 0 , len(A) -1
        rt_list = list()
        while p1 != p2 :
            if abs(A[p2]) >= abs(A[p1]):
                rt_list.append(pow(A[p2],2))
                p2 -= 1
            elif abs(A[p2]) < abs(A[p1]):
                rt_list.append(pow(A[p1],2))
                p1 += 1
        rt_list.append(pow(A[p1],2))
        return rt_list[::-1]