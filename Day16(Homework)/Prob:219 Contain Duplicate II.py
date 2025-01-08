class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ans={}
        for i in range(len(nums)):
            if nums[i] in ans and abs(i-ans[nums[i]])<=k:
                return True
            ans[nums[i]]=i
        return False                         
        
