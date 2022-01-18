class UnionFind:
    # Quick union based union find
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.rank = [1 for i in range(N)]

    def find(self, x):
        # path compression
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        # union by rank
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
