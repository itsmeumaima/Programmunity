class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==0):
            return 0
        nums.sort()
        return ((nums[-1]-1)*(nums[-2]-1))
