from collections import deque
# 1303번 전쟁-전투


def bfs(cr, cc):
    q = deque()
    q.append((cr, cc))
    color = graph[cr][cc]
    visited_list[cr][cc] = True
    cnt = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= M or nc >= N:
                continue
            if graph[nr][nc] != color or visited_list[nr][nc]:
                continue

            cnt += 1
            visited_list[nr][nc] = True
            q.append((nr, nc))

    return cnt


N, M = map(int, input().split())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

graph = []
for _ in range(M):
    graph.append(list(input()))

visited_list = [[False for _ in range(N)] for _ in range(M)]

cntList = [0, 0]
for row in range(M):
    for col in range(N):
        if visited_list[row][col]:
            continue
        res = bfs(row, col)**2
        if graph[row][col] == "W":
            cntList[0] += res
        else:
            cntList[1] += res

print(*cntList)
