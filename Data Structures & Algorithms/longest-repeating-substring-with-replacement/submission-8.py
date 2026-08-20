class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_freq = 0
        freq = {}
        left = 0
        max_length = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(freq[s[r]], max_freq)

            while (r - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_length = max(r - left + 1, max_length)
        return max_length


