class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_list=list(i for i in t)
        s_list=list(i for i in s)
        for i in s_list:
            t_list.remove(i)
        for i in t_list:
            return i  
