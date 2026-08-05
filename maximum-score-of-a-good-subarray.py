class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)

        left = k
        right = k

        minimum = nums[k]
        answer = minimum

        while left > 0 or right < n - 1:

            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] < nums[right + 1]:
                right += 1
            else:
                left -= 1

            minimum = min(minimum, nums[left], nums[right])

            score = minimum * (right - left + 1)
            answer = max(answer, score)

        return answer
