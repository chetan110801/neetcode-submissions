# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         res = float('-inf')
#         for i in range(len(heights)):
#             for j in range(i + 1, len(heights)):
#                 area = min(heights[i], heights[j]) * (j - i)
#                 res = max(res, area)       
#         return res

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, res = 0, len(heights) - 1, 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res




