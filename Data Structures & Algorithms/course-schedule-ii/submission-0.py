from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = list(range(numCourses))
        A = {}
        IN = {}
        OU = {}

        for c in courses:
            A[c] = set()
            IN[c] = 0
            OU[c] = 0

        for c1, c2 in prerequisites:
            A[c1].add(c2)
            OU[c1] += 1
            IN[c2] += 1

        # Run: Topological Sort
        # Khan's Algo
        Q = deque()

        for n, v in IN.items():
            if v == 0:
                Q.append(n)
        
        visited = set()
        dag_ = []

        while Q:
            n = Q.popleft()
            dag_.append(n)
            for nn in A[n]:
                IN[nn] -= 1
                if IN[nn] == 0:
                    Q.append(nn)


        if len(dag_) != numCourses:
            return []
        dag_.reverse()
        return dag_