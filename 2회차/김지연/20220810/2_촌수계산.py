import sys

sys.setrecursionlimit(300000)
sys.stdin = open('2_촌수계산.txt')

n = int(input())
n_1, n_2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
def dfs(start, depth):    
    depth += 1
    visited[start] = True

    if start == n_2:
        result.append(depth)

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth)

dfs(n_1, 0)

if len(result) == 0:
    print('-1')
else:
    print(result[0]-1)