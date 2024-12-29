class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=score[:]
        ans.sort()
        ans=ans[::-1]
        dic={}
        for i in range(len(score)):
            if i==0:
                dic[ans[i]]="Gold Medal"
            elif i==1:
                dic[ans[i]]="Silver Medal"
            elif i==2:
                dic[ans[i]]="Bronze Medal"
            else:
                dic[ans[i]]=str(i+1)
        for i in range(len(score)):
            score[i]=dic[score[i]]
        return score
            
        
