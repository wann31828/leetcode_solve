'''
567. Permutation in String
Medium

Given two strings s1 and s2, write a function to return true if s2 contains 
the permutation of s1. In other words, one of the first 
string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba")

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

'''
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1 is None) or (s2 is None):
            return False
        total = Counter(s1)
        cur = Counter()
        win_str = win_end =  0
        for i in s2:
            cur[i] += 1 
            while len(cur - total) >0 :
                cur[s2[win_str]] -= 1
                if cur[s2[win_str]] ==0:
                    cur.pop(s2[win_str])
                win_str += 1
            if(cur == total):
                return True
            win_end += 1
        return False

foo = Solution()
print(foo.checkInclusion("ab","eidboaoo"))