class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        lst=[]
        for i in range(len(nums)):
            if (nums[i]==1):
                count+=1
            else:
                lst.append(count)
                count=0
        lst.append(count)
        return max(lst)
