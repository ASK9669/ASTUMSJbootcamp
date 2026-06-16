class Solution:
    def reverseWords(self, s: str) -> str:
    
        result= s.split()
        arr = []
        for i in range(len(result)):
            x = result[i]
            y = x[::-1]
            arr.append(y)
        z= " ".join(arr)

        return z



#  AI solutin

    # class Solution:
    #     def reverseWords(self, s: str) -> str:
    #         return " ".join(word[::-1] for word in s.split())
