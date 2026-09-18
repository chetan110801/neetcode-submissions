class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod, zero_count, res = 1, 0, [0] * len(nums)

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num

        if zero_count >= 2:
            return res

        for i, n in enumerate(nums):
            if zero_count: res[i] = 0 if n else prod
            else: res[i] = prod // n

        return res