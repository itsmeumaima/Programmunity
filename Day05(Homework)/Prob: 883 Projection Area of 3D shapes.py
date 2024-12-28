class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy=0
        yz=0
        xz=0
        for i in range(len(grid)):
            for j in grid[i]:
                if j!=0:
                    xy+=1
            xz += max(grid[i])
        for i in range (len(grid)):
            a = 0
            for j in range (len(grid)):
                a = max(a, grid[j][i])
            yz += a
             
        return xy + xz + yz
        
