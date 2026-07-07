class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Global var to count alltime high
        longest = 1
        # hashSet to remove dues and for o(1) lookups
        numSet = set(nums)
        # in each iter if the num - 1 not in numSet means curr num is a start
        # of sequence so curr streak = 1
        if not nums:
            return 0

        for num in numSet:
            if (num - 1) not in numSet:
                streak = 1
                # streak var is used to iterate on all numbers in arr
                # since it icrements by 1 every time
                # its not just for checking every number in the hashSet
                # its made for checking if the value of the number += 1
                # is in the hashSet
                while (num + streak) in numSet:
                    streak += 1
                # at the end of the loop update the max of the two
                longest = max(streak,longest)
        return longest
            






        