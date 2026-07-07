class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1
            R = len(nums) - 1
            while L < R:
                currSum = nums[i] + nums[L] + nums[R]
                if currSum == 0:
                    
                    currRes = [nums[i],nums[L],nums[R]]
                    if currRes not in res:
                        res.append(currRes)
                    L += 1
                    R -= 1
                elif currSum > 0:
                    R -= 1
                else:
                    L += 1
        return res



