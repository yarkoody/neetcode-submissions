class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R
        while L <= R:
            K = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / K)
            if hours > h:
                L = K + 1
            else:
                R = K - 1
                res = min(res, K)
        return res