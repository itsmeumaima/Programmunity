class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        lst = [["1" for _ in range(3)] for _ in range(3)]
        for i in range(len(moves)):
            r, c = moves[i]
            if i % 2 == 0:
                lst[r][c] = "X"
            else:
                lst[r][c] = "O"

        for i in range(3):
            if lst[i][0] == lst[i][1] == lst[i][2]:
                if lst[i][0] == "X":
                    return "A"
                elif lst[i][0] == "O":
                    return "B"
            if lst[0][i] == lst[1][i] == lst[2][i]:
                if lst[0][i] == "X":
                    return "A"
                elif lst[0][i] == "O":
                    return "B"

        if lst[0][0] == lst[1][1] == lst[2][2]:
            if lst[0][0] == "X":
                return "A"
            elif lst[0][0] == "O":
                return "B"
        
        if lst[0][2] == lst[1][1] == lst[2][0]:
            if lst[0][2] == "X":
                return "A"
            elif lst[0][2] == "O":
                return "B"
        
        for row in lst:
            if "1" in row:
                return "Pending"
        
        return "Draw"
