class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n== nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -n
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    while nums[r] == nums[r + 1] and r > l:
                        r -= 1
        return res

                
            






        



            