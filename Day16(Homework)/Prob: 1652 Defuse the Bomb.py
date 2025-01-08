class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        new=code[:]
        if k>0:
            for i in range(len(code)):
                new[i]=sum(code[(i+j)%n] for j in range(1, k+1))
        elif k==0:
            for i in range(len(code)):
                new[i]=0
        else:
            for i in range(len(code)):
                new[i] = sum(code[(i+j)%n] for j in range(k, 0))
        return new
        
