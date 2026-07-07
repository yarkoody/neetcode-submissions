class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            count_letters = [0] * 26
            for letter in word:
                count_letters[ord(letter) - ord('a')] += 1
            dic[tuple(count_letters)].append(word)
        return list(dic.values())
        


