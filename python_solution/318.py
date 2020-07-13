'''
318. Maximum Product of Word Lengths
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters.
You may assume that each word will contain only lower case letters.
If no such two words exist, return 0.
'''
class Solution:
    #bruce force
    def maxProduct(self, words: List[str]) -> int:
        maxlen = 0
        for i , val1 in enumerate(words):
            for j ,val2 in enumerate(words[i+1:]):
                #setlen = len(set(_ for _ in val1+val2))
                mullen = len(val1) * len(val2)
                if len(set(val1) & set(val2))==0 and (mullen > maxlen):
                    maxlen = mullen
        return maxlen
                    
