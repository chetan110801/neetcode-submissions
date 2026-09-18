class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            tup = tuple(count)

            if tup not in res:
                res[tup] = [s]
            else:
                res[tup].append(s)

        return list(res.values())


