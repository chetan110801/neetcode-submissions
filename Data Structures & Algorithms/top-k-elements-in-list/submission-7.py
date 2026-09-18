import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for a, b in heap:
            res.append(b)

        return res[::-1]


        