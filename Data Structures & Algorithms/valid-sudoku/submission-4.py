class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for square in range(len(board)):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
