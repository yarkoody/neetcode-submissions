class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        
        count = [[] for i in range(len(nums) + 1)]
        for num, frq in dic.items():
            count[frq].append(num)
        print(count)

        res = []
        for i in range(len(count)-1, -1, -1):
            for nums in count[i]:
                # if nums > 0:
                res.append(nums)
                if len(res) == k:
                    return res
        # print(res)
        return res

