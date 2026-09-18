class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        l = []
        for num, count in counts.items():
            l.append((count, num))
        l.sort()

        res = []
        while len(res) < k:
            res.append(l.pop()[1])

        return res

        