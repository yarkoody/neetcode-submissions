class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            L = 0
            R = len(row) - 1
            while L <= R:
                mid = (L + R) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    L = mid + 1
                else:
                    R = mid -1
        return False
            