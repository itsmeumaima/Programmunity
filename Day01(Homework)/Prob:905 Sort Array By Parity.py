class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst1=[]
        lst2=[]
        for i in nums:
            if (i%2==0):
                lst1.append(i)
            else:
                lst2.append(i)
        return lst1+lst2
