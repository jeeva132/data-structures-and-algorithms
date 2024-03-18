class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(cur):

            if cur in visited:
                return False
            if preMap[cur] == []:
                return True
            
            visited.add(cur)

            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            visited.remove(cur)
            preMap[cur] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True
        
        
