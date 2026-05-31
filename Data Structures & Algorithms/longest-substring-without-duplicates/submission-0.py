class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        maxLen = 0

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

            while seen[s[i]] > 1:
                seen[s[start]] -= 1
                start += 1
            
            if (i-start+1) > maxLen:
                maxLen = (i-start+1)

        return maxLen