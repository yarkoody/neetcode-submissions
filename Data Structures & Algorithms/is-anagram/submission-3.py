class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicS = {}
        dicT = {}

        for char in s:
            dicS[char] = dicS.get(char,0) + 1

        for char in t:
            dicT[char] = dicT.get(char,0) + 1

        if dicS == dicT:
            return True
        return False