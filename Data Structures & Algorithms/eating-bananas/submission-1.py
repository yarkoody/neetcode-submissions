import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        left = 1
        right = max(piles)
        best_k = float("inf")
        while left <= right:
            k = (left+right) // 2
            total_hours = 0

            for pile in piles:
                time_to_eat = math.ceil((pile / k))
                total_hours += time_to_eat
            if total_hours > h:
                left = k + 1
            elif total_hours <= h:
                best_k = min(best_k, k)
                right = k - 1
        return best_k

                
            


