class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        maxlen = 0
        start = 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[start])
                start += 1
            
            visited.add(s[i])

            if (i-start+1) > maxlen:
                maxlen = (i-start+1)
        return maxlen