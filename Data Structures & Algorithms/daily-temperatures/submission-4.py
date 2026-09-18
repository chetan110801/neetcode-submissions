class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break

        return res
                

        # res = [0] * len(temperatures)
        # stack = []

        # for i, t in enumerate(temperatures):
        #     while stack and stack[-1][0] < t:
        #         stackT, stackIdx = stack.pop()
        #         res[stackIdx] = i - stackIdx
        #     stack.append((t, i))

        # return res
        