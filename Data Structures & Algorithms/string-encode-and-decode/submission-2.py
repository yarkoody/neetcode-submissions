class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            length = len(word)
            res += f"{length}#{word}"
        # print(res)
        return res


    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            print(f"length{length}")
            word = s[j+1: j+1 + length]
            print(word) 
            decoded.append(word)
            i = j + 1 + length
        return decoded



