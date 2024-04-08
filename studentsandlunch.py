class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = collections.deque(students)

        for sandwich in sandwiches:
            if sandwich in q:
                while q[0] != sandwich:
                    x = q.popleft()
                    q.append(x)
                q.popleft()
            else:
                return len(q)
        return 0
