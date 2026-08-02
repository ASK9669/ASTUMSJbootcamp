class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arre =[]
        for i in range(len(image)):
            x = image[i]
            x.reverse()
            y = []
            for j in range(len(x)):
                if x[j] == 0:
                    y.append(1)
                else:
                    y.append(0)
            arre.append(y)
        return (arre)
