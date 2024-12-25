class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        new=[]
        for i in image:
            result=[1-j for j in i[::-1]]
            new.append(result)
        return new            

        
