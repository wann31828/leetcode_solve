'''
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
#sliding window
from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        win_str , win_end = 0,0
        maxlen = -float('inf')
        c = Counter()

        for i in range(len(s)):
            c.update(s[i])
            while len(c.keys()) != sum(c.values()):
                c.subtract(s[win_str])
                if c[s[win_str]] == 0:
                    c.pop(s[win_str])
                win_str += 1
            
            maxlen = max(maxlen,len(c.keys()))
            win_end += 1
        
        return (0 if maxlen < 0 else maxlen)

obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew")) #3