class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            ans+=mat[i][i]
            if i!=len(mat)-1-i:
                ans+=mat[i][len(mat)-1-i]
        return ans
