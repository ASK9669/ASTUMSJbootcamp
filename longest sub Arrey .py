class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        z = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
            while z > 1:
                if nums[left] == 0:
                    z -= 1
                left += 1
            ans = max(ans, i - left)
        return ans
