class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i,n in enumerate(words):
            if x in n:
                arr.append(i)
        return arr
