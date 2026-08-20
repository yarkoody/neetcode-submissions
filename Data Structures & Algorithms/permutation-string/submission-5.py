class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = {}
        for char in s1:
            s1_d[char] = s1_d.get(char,0) + 1
        
        window_size = len(s1)
        if window_size > len(s2):
            return False

        window = {}
        for r in range(window_size):
            window[s2[r]] = window.get(s2[r],0) + 1
        if window == s1_d:
            return True
        for r in range(window_size, len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            left_char = s2[r - window_size]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            if window == s1_d:
                return True
        return False


