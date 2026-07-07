class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        maxWater = 0
        while L < R:
            width = R-L
            height = min(heights[L],heights[R])
            
            currMax = height * width
            maxWater = max(currMax,maxWater)
            if heights[L] <= heights[R]:
                L += 1
            else: 
                R -= 1
        return maxWater

