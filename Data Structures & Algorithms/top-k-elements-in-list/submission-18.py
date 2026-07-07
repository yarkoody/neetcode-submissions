class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in (nums):
            dic[num] = dic.get(num,0) + 1
        
        freq_arr = [[] for i in range(len(nums)+1)]
        for num, frq in dic.items():
            freq_arr[frq].append(num)
        print(freq_arr)
        result = []
        n = len (freq_arr)
        for i in range(n-1,-1,-1):
            for num in freq_arr[i]:
                result.append(num)
            if len(result) == k:
                return result

        