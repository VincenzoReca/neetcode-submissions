class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s)-1
        left = 0
        s_clean = s.lower()
        while left < right:

            if not s_clean[left].isalnum():
                left += 1
                continue

            if not s_clean[right].isalnum():
                right -= 1
                continue

            if s_clean[left] != s_clean[right]:
                return False

            left += 1
            right -= 1

        return True