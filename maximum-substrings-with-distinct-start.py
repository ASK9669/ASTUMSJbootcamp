class Solution:
    def maxDistinct(self, s: str) -> int:
        result =[]
        for ch in s:
            if ch not in result:
                result.append(ch)
        return len(result)       
