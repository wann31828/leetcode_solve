'''
118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of 
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers
directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        sol = []
        for i in range(1,numRows+1):
            if i == 1:
                sol.append([1])
            elif i == 2:
                sol.append([1,1])
            else:
                cur = []
                for j in range(i):
                    if j ==0 or j == i-1:
                        cur.append(1)
                    else:
                        cur.append(sol[i-2][j-1]+sol[i-2][j])
                        #i[n] = i-1[n-1] + i-1[n]
                sol.append(cur)
        return sol
        

