class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t ={}
        for letter in s:
            letters_s[letter] = letters_s.get(letter,0) + 1
        for letter in t:
            letters_t[letter] = letters_t.get(letter,0) + 1
        
        return letters_s == letters_t
            