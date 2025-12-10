from heapq import heappush, heappop

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        self.size[px] += self.size[py]
        
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True
    
    def get_size(self, x):
        return self.size[self.find(x)]
    
    def get_all_sizes(self):
        root_sizes = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in root_sizes:
                root_sizes[root] = self.size[root]
        return list(root_sizes.values())

def distance_squared(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2))

with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

junctions = []
for line in lines:
    x, y, z = map(int, line.split(','))
    junctions.append((x, y, z))

n = len(junctions)
print(n)

edges = []
for i in range(n):
    for j in range(i + 1, n):
        dist_sq = distance_squared(junctions[i], junctions[j])
        heappush(edges, (dist_sq, i, j))

uf = UnionFind(n)
connections_made = 0
attempted = 0

while edges and attempted < 1000:
    dist_sq, i, j = heappop(edges)
    attempted += 1
    if uf.union(i, j):
        connections_made += 1

sizes = uf.get_all_sizes()
sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])

uf2 = UnionFind(n)
last_i, last_j = None, None

edges2 = []
for i in range(n):
    for j in range(i + 1, n):
        dist_sq = distance_squared(junctions[i], junctions[j])
        heappush(edges2, (dist_sq, i, j))

num_components = n
while edges2 and num_components > 1:
    dist_sq, i, j = heappop(edges2)
    if uf2.union(i, j):
        last_i, last_j = i, j
        num_components -= 1

result = junctions[last_i][0] * junctions[last_j][0]
print(result)
