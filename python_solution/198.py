'''
198. House Robber

Input: nums = [2,7,9,3,1]
Output: 12

n= 0 :
dp[0] = nums[0] 

n= 1 :
dp[1] = max( nums[0], nums[1])

when n>2：
dp[i] = max( dp[i-2] + nums[i], dp[i-1])
'''


def rob(thelist):
    if not thelist:
        return 0
    dplist = []
    for i, val in enumerate(thelist):
        if i == 0:
            dplist.append(val)
        elif i == 1:
            dplist.append(max(thelist[0], val))
        else:
            dplist.append(max(dplist[i-1], dplist[i-2]+val))
    return max(dplist[-2:])
