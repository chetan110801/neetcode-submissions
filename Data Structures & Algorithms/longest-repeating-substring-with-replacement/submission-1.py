class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                while (j-i+1) - max(count.values()) > k:
                    count[s[i]] -= 1
                    i += 1
                res = max(res, j-i+1)

        return res


        