'''
345. Reverse Vowels of a String
Write a function that takes a string as input and reverse
only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        volist = []
        mylist = list(s)
        for i , val in enumerate(mylist):
            if val in vowels:
                volist.append(i)
        
        for i in range(int(len(volist)/2)):
            tmp = mylist[volist[i]]
            mylist[volist[i]] = mylist[volist[-i-1]]
            mylist[volist[-i-1]] = tmp
        
        return ''.join(mylist)