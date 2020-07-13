'''
231. Power of Two
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: pow(2,0)= 1

'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0 :
            return False
        return bin(n).count('1') == 1