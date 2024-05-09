class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mcandies = max(candies)

        gcandies = []

        for c in candies:
            gcandies.append(c+extraCandies >= mcandies)

        return gcandies
