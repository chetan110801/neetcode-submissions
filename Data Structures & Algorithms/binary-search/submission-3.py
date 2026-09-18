class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums) - 1, nums, target)

    def bs(self, l, r, nums, target):
        if l > r:
            return -1
        m = l + (r - l) // 2
        if target == nums[m]:
            return m
        if target < nums[m]:
            return self.bs(l, m - 1, nums, target)
        return self.bs(m + 1, r, nums, target)
        



        