class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s)-1
        left = 0
        tmp = ""
        while left < right:
            tmp = s[right]
            s[right] = s[left]
            s[left] = tmp
            right -= 1
            left += 1