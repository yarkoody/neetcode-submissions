class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sortedW = ''.join(sorted(word))
            result[sortedW].append(word)
        return list(result.values())