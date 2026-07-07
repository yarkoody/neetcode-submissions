class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            # still at the big section
            # need to move to smaller section the def starts after mid

            if nums[mid] > nums[R]:
                L = mid + 1
            
            else:
                R=mid
        return nums[R]