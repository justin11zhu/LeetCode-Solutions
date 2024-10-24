#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = dict()
        result = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = i
                result = max(result, i - left + 1)
            else:
                if chars[s[i]] < left:
                    result = max(result, i - left + 1)
                else:
                    left = chars[s[i]] + 1
                chars[s[i]] = i

        return result

            
        
        return result