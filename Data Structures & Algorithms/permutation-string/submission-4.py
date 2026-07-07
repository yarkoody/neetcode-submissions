class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        window = [0] * 26
        
        for char in s1:
            s1Count[ord(char) - ord('a')] += 1
        
        L = 0
        for R in range(len(s2)):
            if (R-L+1) > len(s1):
                window[ord(s2[L])-ord('a')] -= 1
                L+=1
            window[ord(s2[R])-ord('a')] += 1
            
            if window == s1Count:
                return True

        return False
        


        