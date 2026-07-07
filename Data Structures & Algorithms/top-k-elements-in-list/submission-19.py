class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hist = {}
        for num in nums:
            hist[num] = hist.get(num,0) + 1
        sorted_keys = sorted(hist, key=hist.get,reverse=True)
        return sorted_keys[:k]


