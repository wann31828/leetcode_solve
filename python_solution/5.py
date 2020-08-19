'''
5. Longest Palindromic Substring
Medium

7529

561

Add to List

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

#DP
'''
dp[i, j]   = 1                                               if i == j

           = s[i] == s[j]                                if j = i + 1

           = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1   
'''

import itertools
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N == 0:
            return ""
        left , length = 0,1
        temp = itertools.count(0,0)
        dp = [[next(temp) for i in range(N)] for i in range(N)]
        for i in range(N):
            dp[i][i] = 1
            for j in range(i):
                dp[j][i] = ((s[i] == s[j]) and (i-j<2 or dp[j+1][i-1]))
                if dp[j][i] and (length < i -j +1):
                    length = i -j +1
                    left = j

        return s[left:left+length]
