"""
no.137
Given a non-empty array of integers, every element appears three times
except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
-----------------------------------------------------------------
Input: [0,1,0,1,0,1,99]
Output: 99
"""
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums :
        return None
    for i in nums:
        if nums.count(i) == 1:
            return i


def singleNumber_dict(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return None

    mydict = dict()
    for i in nums:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    
    for key , val in mydict.items():
        if val !=3:
            return key

'''
No 121
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


'''
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    s_prices = sorted(prices)
    l ,r = 0 , len(s_prices)-1
    min_val , max_val = s_prices[l] ,s_prices[r]
    max_profile = max_val - min_val
    while True:
        if prices.index(min_val) > prices.index(max_val):
            if (s_prices[r-1] - s_prices[l]) > (s_prices[r] - s_prices[l+1]):
                r -= 1
            else:
                l += 1
            min_val , max_val = s_prices[l] ,s_prices[r]
        else:
            return max_val - min_val
'''

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxpfofiles = 0
    minchoice = float('inf')

    for i in prices:
        if i < minchoice:
            minchoice = i
        maxpfofiles = max(i-minchoice , maxpfofiles)



        
