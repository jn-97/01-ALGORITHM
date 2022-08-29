import sys

sys.setrecursionlimit(300000)
sys.stdin = open('3_섬의 개수.txt')

def dfs(x, y):
    if x < 0 or y < 0 or y >= w or x >= h:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x, y-1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        dfs(x, y+1)
        dfs(x-1, y+1)
        return True
    return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else: 
        result = 0
        graph = [] 
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        for i in range(h):
            for j in range(w):
                if dfs(i, j) == True:
                    result += 1
        print(result)