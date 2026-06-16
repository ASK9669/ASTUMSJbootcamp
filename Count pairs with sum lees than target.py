class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        x = 0
        y = len(nums)-1
        while x < y:
            if nums[x]+nums[y] < target:
                count  += y-x
                x +=1
            else:
                y -= 1
        return count

# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         count = 0

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] < target:
#                     count += 1

#         return count
