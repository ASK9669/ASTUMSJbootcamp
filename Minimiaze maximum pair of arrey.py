class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        x = len(nums)-1
        for i in range(len(nums)):
            result.append(nums[i]+nums[x])
            x -=1
        max1 = max(result)
        return max1
         
