class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        arr = []
        for num, count in counts.items():
            arr.append((count, num))

        res = []
        for ele in arr:
            heapq.heappush(res, ele)
            if len(res) > k:
                heapq.heappop(res)

        output = []
        for i in range(k):
            output.append(heapq.heappop(res)[1])

        return output


        