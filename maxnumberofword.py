class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        newa = [i.split(' ') for i in sentences]
        count = 0
        max1 = 0
        for i in newa:
            for j in i:
                count +=1

            max1 = max(count,max1)
            count = 0
        return max1
        
