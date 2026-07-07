class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def pivot(arr):
            left = 0
            right = len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > arr[right]:
                    left = mid + 1
                else:
                    right = mid
            return left  # ✅ FIXED from 'return right'

        n = len(nums)
        p = pivot(nums)

        # Decide which part to search: left or right of the pivot
        if nums[p] <= target <= nums[n - 1]:
            L = p
            R = n - 1
        else:
            L = 0
            R = p - 1

        # Standard binary search
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1
