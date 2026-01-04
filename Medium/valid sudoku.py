class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        vert = set()
        horz = set()
        for i in range(9):# check repitition
            vert = set()
            horz = set()
            for j in range(9):
                if board[i][j] not in vert:
                    vert.add(board[i][j])
                elif board[i][j] != '.':
                    return False
                if board[j][i] not in horz:
                    horz.add(board[j][i])
                elif board[j][i] != '.':
                    return False
        for i in range(9):
            small_box = set()
            print("square: ",i)
            for j in range(9):
                row = (j%3) +(i % 3) * 3
                col = (j//3) +(i // 3) * 3
                if board[row][col] not in small_box:
                    small_box.add(board[row][col])
                elif board[row][col] != '.':
                    return False

                
        return True