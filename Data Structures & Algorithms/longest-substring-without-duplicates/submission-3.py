class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        seen = set()
        longest = 0
        # check every char
        for R in range(len(s)):
            # if we have seen the char already meaning its a dupe
            # we need to decrese the window by moving the L pointer
            # change the seen hashset so the window size is valid and contains only unique characters
            
            while s[R] in seen:
                
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            longest = max(longest, R - L + 1)
        return longest