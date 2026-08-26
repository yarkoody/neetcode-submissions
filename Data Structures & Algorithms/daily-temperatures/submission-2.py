class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                days_passed = i - index
                days[index] = days_passed
            stack.append(i)
        return days
