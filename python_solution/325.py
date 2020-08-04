'''
LeetCode 325. Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
'''

#Maximum Subarray Problem , store sum -k at hashmap
from collections import defaultdict
def maxSubArrayLen(nums,k):
    sum_dict = defaultdict(list)
    localsum = maxlen = 0
    for i,val in enumerate(nums):
        localsum +=val
        if localsum == k:
            maxlen = i+1
        else:
            if (localsum - k) in sum_dict:
                maxlen = max(maxlen , i - sum_dict[localsum - k][0])
            else:
                sum_dict[localsum].append(i)
    return maxlen

print(maxSubArrayLen([2,0,2,1,1,1],  3)) #rt: 3
print(maxSubArrayLen([-2, -1, 2, 1], 1))  # rt:2
print(maxSubArrayLen([1, -1, 5, -2, 3], 3)) #rt : 4
