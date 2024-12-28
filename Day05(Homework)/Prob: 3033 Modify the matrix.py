class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        temp=[max(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
        answer=matrix[::]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    if matrix[i][j]==-1:
                        answer[i][j]=temp[j]
        return answer
