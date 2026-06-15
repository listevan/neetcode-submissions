class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []

        for i, temp in enumerate(temperatures):
            while s and temp > temperatures[s[-1]]:
                j = s.pop()
                result[j] = i-j
            s.append(i)

        return result