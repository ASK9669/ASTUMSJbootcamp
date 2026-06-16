class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # nums.sort()
        result = []
        for i in nums:
            if i < pivot:
                result.append(i)
        for i in nums:
            if i == pivot:
                result.append(i)
        for i in nums:
            if i > pivot:
                result.append(i)

        return result
 
