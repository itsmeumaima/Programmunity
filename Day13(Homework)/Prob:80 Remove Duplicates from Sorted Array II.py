class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp={}
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        for i in temp.keys():
            while temp[i]>2:
                nums.remove(i)
                temp[i]-=1
        return len(nums)
        
