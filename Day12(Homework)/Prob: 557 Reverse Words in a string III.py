class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=s.split()
        ans=" ".join(i[::-1] for i in new)
        return ans
        
