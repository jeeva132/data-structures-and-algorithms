class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            k = 0
        elif ruleKey == 'color':
            k = 1
        else:
            k = 2
        count = 0

        for i in items:
            if i[k] == ruleValue:
                count +=1
        return count
