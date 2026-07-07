class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
             return []
        hist = {}
        for num in nums:
            hist[num] = hist.get(num,0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in hist.items():
            buckets[freq].append(num)

        result = []
        
        for freq in range(len(buckets) - 1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
            





