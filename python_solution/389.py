'''
389. Find the Difference

Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then
add one more letter at a random position. 
Find the letter that was added in t.

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictA = {} 
        for i in t:
            if(dictA.get(i)):
                dictA[i]+=1
            else:
                dictA[i] = 1
        
        for i in s:
            dictA[i] -= 1
        
        for i , val in dictA.items():
            if val == 1:
                return i
        
