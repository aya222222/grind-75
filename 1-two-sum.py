class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums):
              if idx2 == idx: 
                 break

              if target - num == num2:
                 return [idx, idx2]   