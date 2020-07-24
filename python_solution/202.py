'''
202. Happy Number
Easy

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
#hash
from collections import defaultdict
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = defaultdict(lambda : 0)
        tot = 0
        if n == pow(10,len(str(n))-1):
            return True
        while True:
            for i in str(n) :
                tot += pow(int(i),2)
            if tot == pow(10,len(str(tot))-1) :
                return True
            elif tot in record:
                return False
            else :
                record[tot] +=1
                n = tot
                tot = 0
    

# fast , slow  pointer
class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast = slow = n
        if n == pow(10,len(str(n))-1):
            return True
        
        while True:
            slow = sum([pow(int(i),2) for i in str(slow)])
            fast = sum([pow(int(i),2) for i in str(fast)])
            fast = sum([pow(int(i),2) for i in str(fast)])
            if slow == fast :
                if slow == pow(10,len(str(slow))-1) :
                    return True               
                else:
                    return False

foo = Solution2()
print(foo.isHappy(19)) #expect:True 
print(foo.isHappy(7)) #expect:True 