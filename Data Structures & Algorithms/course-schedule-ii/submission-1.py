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

        def topological_sort_dfs(A):
            # 0 = Unvisited, 1 = Visiting (in path), 2 = Visited (done)
            state = {i: 0 for i in A.keys()}
            stack = []
            
            def dfs(u):
                state[u] = 1 # Mark as visiting
                
                for v in A[u]:
                    if state[v] == 1:       # Cycle detected
                        return False
                    if state[v] == 0:       # Visit unvisited neighbor
                        if not dfs(v):
                            return False
                            
                state[u] = 2 # Mark as fully processed
                stack.append(u)
                return True

            # Process every node to handle disconnected graph components
            for i in A:
                if state[i] == 0:
                    if not dfs(i):
                        return []
                        
            return stack[::-1] # Reverse the stack to get the correct order

        stack = topological_sort_dfs(A)
        stack.reverse()

        return stack if len(stack)==numCourses else []