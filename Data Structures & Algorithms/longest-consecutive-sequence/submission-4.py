class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        res = 0

        for n in numSet:
            streak = 1
            while n + streak in numSet:
                streak += 1
            res = max(res, streak)

        return res


                




        