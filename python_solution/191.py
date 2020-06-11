'''Write a function that takes an unsigned integer and return
the number of '1' bits it has
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n))[2:].count('1')