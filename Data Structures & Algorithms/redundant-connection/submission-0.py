class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.cycles = []

    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node

    def union(self, nodeA, nodeB):
        parA, parB = self.find(nodeA), self.find(nodeB)

        if parA == parB:
            self.cycles.append([nodeA, nodeB])
            return
       
        if self.rank[parA] < self.rank[parB]:
            self.par[parA] = parB
            self.rank[parB] += self.rank[parA]
        else:
            self.par[parB] = parA
            self.rank[parA] += self.rank[parB]

        return 
    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for src, dst in edges: 
            uf.union(src, dst) 

        return uf.cycles[-1]