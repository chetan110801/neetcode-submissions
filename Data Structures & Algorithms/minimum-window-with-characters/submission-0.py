class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t: return ''

        countT, windowS = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            windowS[c] = 1 + windowS.get(c, 0)

            if c in countT and windowS[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                windowS[s[l]] -= 1
                if s[l] in countT and windowS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return "" if resLen == float('inf') else s[l : r + 1]



        
