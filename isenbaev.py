n = int(input())
d = {}
for i in range(n):
    arr = input().split()
    for j in range(len(arr)):
        for z in range(j + 1, len(arr)):
            if d.get(arr[j]) is None:
                d[arr[j]] = set()
            if d.get(arr[z]) is None:
                d[arr[z]] = set()
            d[arr[j]].add(arr[z])
            d[arr[z]].add(arr[j])



used = {}

visited = {}
prev = {}


def dfs(start, visited, prev, g, i):
    print(start, i)
    visited[start] = True
    for u in g[start]:
        if not visited.get(u):
            prev[u] = start
            dfs(u, visited, prev, g, i)
            i += 1


dfs('Isenbaev', visited, prev, d, 0)
