class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        ans=[grid[i][j] for i in range(m) for j in range(n)]
        k=k%(m*n)
        ans=ans[-k:]+ans[:-k]
        result=[[ans[i*n+j] for j in range(n)] for i in range(m)]
        return result
