class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)

        for crs, pre_req in prerequisites:
            indegree[crs] += 1
            graph[pre_req].append(crs)

        deq = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while deq:
            crs = deq.popleft()
            taken += 1

            for neigh in graph[crs]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    deq.append(neigh)

        return taken == numCourses