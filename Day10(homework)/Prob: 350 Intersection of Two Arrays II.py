class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        i=0
        while (nums1!=[] and i<len(nums1)):
            if nums1[i] in nums2:
                val=nums1[i]
                ans.append(val)
                nums1.remove(val)
                nums2.remove(val)
            else:
                i+=1
        return  ans
        
