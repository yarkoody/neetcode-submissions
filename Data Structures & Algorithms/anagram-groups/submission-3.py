class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        dic = defaultdict(list)

        for word in strs:
            count = 26 * [0]
            for char in word:
                count[ord(char)-ord('a')] += 1
            dic[tuple(count)].append(word)
        return list(dic.values())
        
                

