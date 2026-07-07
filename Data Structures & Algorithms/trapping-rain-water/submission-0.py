class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0 :
            return 0

        # leftMax = [0] * n
        # # rightMax = [0] * n
        L = 0
        R = n - 1
        maxL = height[L]
        maxR = height[R]
        res = 0

        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(height[L], maxL)
                res += maxL - height[L]
            else:
                R -= 1
                maxR = max(maxR, height[R])
                res += maxR - height[R]
        return res
        
        # for i in range(1,n):
        #     leftMax[i] = max(height[i],leftMax[i - 1])

        # rightMax[n-1] = height[n-1]
        # for i in range(n - 2, -1, -1):
        #     rightMax[i] = max(height[i],rightMax[i+1])

        # res = 0
        # for i in range(n):
        #     res += min(leftMax[i],rightMax[i]) - height[i]
        # return res