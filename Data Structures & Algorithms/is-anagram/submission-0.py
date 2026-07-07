class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for letter in s:
            if letter in dic_s:
                dic_s[letter] += 1
            else:
                dic_s[letter] = 1
        for letter in t:
            if letter in dic_t:
                dic_t[letter] += 1
            else:
                dic_t[letter] = 1
        if dic_s == dic_t:
            return True
        else:
            return False
