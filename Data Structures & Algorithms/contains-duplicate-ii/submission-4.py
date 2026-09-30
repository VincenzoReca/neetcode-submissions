class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                j = seen.get(num)
                if abs(i-j) <= k:
                    return True
                
            seen[num] = i
        return False