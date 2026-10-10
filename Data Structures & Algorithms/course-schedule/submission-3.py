class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        A = defaultdict(set)
        OD = defaultdict(int)
        ID = defaultdict(int)
        for s, p in prerequisites:
            A[s] = set()
            A[p] = set()
            ID[s] = 0
            ID[p] = 0

        for s, p in prerequisites:
            A[s].add(p)
            OD[p] += 1
            ID[s] += 1

        # START: Detect Cycle
        visited = set()
        rec_stack = set()  # Tracks nodes in the current path
        def has_cycle(s) -> bool:
            # If it is in the current path, we found a cycle
            if s in rec_stack:
                return True
            # If already fully processed and not in path, skip it
            if s in visited:
                return False

            rec_stack.add(s)
            visited.add(s)

            for n in A[s]:
                if has_cycle(n):
                    return True

            rec_stack.remove(s)  # Backtrack: remove from current path
            return False
        # END: Detect Cycle
        id_0 = list(filter(lambda x: ID[x] == 0, ID.keys()))
        if not id_0:
            return False

        if has_cycle(id_0[0]):
            return False

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
        print(stack)
        return len(stack) > 0
