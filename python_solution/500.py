'''
500. Keyboard Row
Easy

Given a List of words, return the words that can be typed using letters
of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.

'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        q_set = set("qwertyuiop")
        a_set = set("asdfghjkl")
        z_set = set("zxcvbnm")

        ok_list = list()
        for word in words:
            word_set = set(word.lower())
            if not (word_set - q_set and word_set -a_set and word_set - z_set):
                ok_list.append(word)
        
        return ok_list