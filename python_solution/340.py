from collections import Counter

'''
340. Longest Substring with At Most K Distinct Characters
Hard
s = eceba , k= 2 
output =3
'''
#sliding window
def lengthOfLongestSubstringKDistinct( s, k) :
    '''
    string : s
    int : k
    rt : int
    '''

    mydict = Counter()
    wind_str , win_end = 0 , 0
    maxlen = -float('inf')

    for i in range(len(s)):
        mydict.update(s[i])
        while len(mydict.keys()) >k:
            mydict.subtract(s[wind_str])
            if mydict[s[wind_str]] <= 0:
                mydict.pop(s[wind_str])
            wind_str +=1

        if len(mydict.keys()) ==k:
            maxlen = max(maxlen,sum(mydict.values()))
        win_end += 1
    
    return (0 if maxlen < 0 else maxlen)

print(lengthOfLongestSubstringKDistinct("abcbbbbcccbdddadacb",2)) #3
