from pprint import pprint
import sys
sys.setrecursionlimit(5000)
sys.stdin = open('1_연결 요소의 개수.txt')

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start, depth):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i, 0)
            cnt += 1

print(cnt)