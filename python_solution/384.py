
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori_dataset = nums
        self.dataset = self.ori_dataset[:]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.dataset = self.ori_dataset[:]
        return self.dataset

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.dataset)
        return self.dataset