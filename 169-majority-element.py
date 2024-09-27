class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math

        half = math.floor(len(nums)/2) + 1
        

        numDict = dict()
        for num in nums :
          if num in numDict:
            numDict[num]=numDict[num]+1    
        
          else:
            numDict[num] = 1
        
          if numDict[num] >= half:
             return num
          

       