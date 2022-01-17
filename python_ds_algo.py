class UnionFind:
    # Quick union by rank
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
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
    
