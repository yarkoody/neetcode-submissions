class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        L = 0
        maxf = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R],0) + 1
            maxf = max(maxf, count[s[R]])
            # get the maximum freq of max and the curr char
            
            while (R - L + 1) - maxf > k:
                count[s[L]] -= 1
                L+=1
            res = max(R - L + 1,res)
        return res
            
            

