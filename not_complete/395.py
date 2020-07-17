'''
395. Longest Substring with At Least K Repeating Characters
Medium

Find the length of the longest substring T of a given string
(consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times
and 'b' is repeated 3 times.
'''

from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        remain_counter_dict = Counter(s)
        
        cur_counter_dict = Counter()
        winsize = 0
        rt = float('-inf')

        for i in s:
            if(remain_counter_dict[i]) >= k:
                cur_counter_dict[i] += 1
                winsize += 1
                if all(list(map(lambda a : a>=k ,cur_counter_dict.values()))):
                    rt = max(rt,winsize)
            else:
                remain_counter_dict -= cur_counter_dict
                cur_counter_dict -= cur_counter_dict
                winsize = 0
        return (rt if rt > float('-inf') else 0)

a = Solution()
print(a.longestSubstring("ababbc",2))  
#fialed in test case "bbaaacbd" , 3      