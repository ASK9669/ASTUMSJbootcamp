class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = set(nums1)
        y = set(nums2)
        result = []
        for i in x:
            if i in y:
                result.append(i)
        return result


    # AI Solution
    # class Solution:
    #     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #         return list(set(nums1).intersection(set(nums2)))
