class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort()
        n = len(stones)

        while n > 1:
            c = stones.pop() - stones.pop()
            n -= 2
            if c > 0:
                l, r = 0, n
                while l < r:
                    m = (l + r) // 2
                    if stones[m] < c:
                        l = m + 1
                    else:
                        r = m 
                pos = l
                n += 1
                stones.append(0)
                for i in range(len(stones) - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = c

        return stones[0] if stones else 0
        