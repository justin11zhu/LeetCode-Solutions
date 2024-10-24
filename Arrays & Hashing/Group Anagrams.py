#https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            cur = [0] * 26
            for char in word:
                cur[ord(char) - ord('a')] += 1
            if tuple(cur) not in anagrams:
                anagrams[tuple(cur)] = [word]
            else:
                anagrams[tuple(cur)].append(word)
        return anagrams.values()

