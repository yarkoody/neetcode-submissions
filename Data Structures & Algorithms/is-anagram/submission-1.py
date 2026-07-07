class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicS = {}
        dicT = {}
        for letter in s:
            dicS[letter] = dicS.get(letter,0) + 1
        
        for letter in t:
            dicT[letter] = dicT.get(letter,0) + 1

        if dicS == dicT:
            return True
        return False


