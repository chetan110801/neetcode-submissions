class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mr = (top + bot) // 2
            if matrix[mr][0] > target:
                bot = mr - 1
            elif matrix[mr][-1] < target:
                top = mr + 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mc = (l + r) // 2
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] > target:
                r = mc - 1
            else:
                l = mc + 1
        return False


        
