class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            val=nums[i]**2
            ans.append(val)
        ans.sort()
        return ans
      
