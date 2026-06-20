class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 1 or nums[i] > threshold:
                continue

            length = 1
            ans = max(ans, length)

            for j in range(i + 1, n):
                if nums[j] > threshold:
                    break

                if nums[j] % 2 == nums[j - 1] % 2:
                    break

                length += 1
                ans = max(ans, length)

        return ans