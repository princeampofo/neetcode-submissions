class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)

        for crs, pre_req in prerequisites:
            indegree[crs] += 1
            graph[pre_req].append(crs)

        deq = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while deq:
            crs = deq.popleft()
            res.append(crs)

            for neigh in graph[crs]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    deq.append(neigh)

        return res if len(res) == numCourses else []