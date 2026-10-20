class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.components = n

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, nodeA, nodeB):
        parA = self.find(nodeA)
        parB = self.find(nodeB)

        if parA == parB:
            return False

        if self.rank[parB] > self.rank[parA]:
            self.parent[parA] = parB
            self.rank[parB] += self.rank[parA]
        else:
            self.parent[parB] = parA
            self.rank[parA] += self.rank[parB]

        self.components -= 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        uf = UnionFind(n)

        for src, dst in edges:
            if not uf.union(src, dst):
                return False

        return uf.components == 1
        