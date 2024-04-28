class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] is stones[j]:
                    total +=1

        return total
