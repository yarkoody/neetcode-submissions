class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS =  26 * [0]
        countT =  26 * [0]
        for char in s:
            countS[ord(char)-ord('a')] += 1
            print(ord(char))
        for char in t:
            countT[ord(char)-ord('a')] += 1
        if countS == countT:
            return True
        return False

