class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                # create an histogram of the alphabet letters that are in use in the word
                count[ord(char)-ord('a')] += 1
            # make the histogram as a key, and append the word that fits the histogram.
            res[tuple(count)].append(word)
        return list(res.values())