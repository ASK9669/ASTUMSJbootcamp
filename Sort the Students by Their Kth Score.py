class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # result = []
        # arr =[]
        # for i in range(len(score)):
        #     result.append(score[i][k])
        # result.sort()
        # result.reverse()
        # for i in result:
        #     if i in score[i]:
        #         arr.append(i)
        # return arr
         
        result = []

        for i in range(len(score)):
            result.append(score[i])

            result.sort(key=lambda x: x[k])
        result.reverse()

        return result
