class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for cur_day, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = cur_day - prev_day

            stack.append(cur_day)
        return res

