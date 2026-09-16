class Solution(object):
    def isValidSudoku(self, board):
        rows=[[False]*9 for _ in range(9)]
        col=[[False]*9 for _ in range(9)]
        cell=[[False]*9 for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val=='.':
                    continue
                i=int(val)-1
                x=(r//3)*3+(c//3)
                if rows[r][i] or col[c][i] or cell[x][i]:
                    return False
                rows[r][i]=col[c][i]=cell[x][i]=True
        return True
s = Solution()

valid_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(valid_board))
