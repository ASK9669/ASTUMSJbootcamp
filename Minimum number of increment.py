class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        c =target[0]
        for x in range(1,len(target)):
            if target[x] > target[x-1]:
                c +=  target[x] - target[x-1]
        return c
        
