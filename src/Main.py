# 2098번 외판원 순회
def dfs(now, visited):
    if visited == (1 << N) - 1:
        if graph[now][0]:
            return graph[now][0]
        else:
            return int(1e9)

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = int(1e9)
    for nxt in range(1, N):
        # print(bin(visited), bin(nxt), bin(1 << nxt), visited & (1 << nxt))
        if graph[now][nxt] == 0 or visited & (1 << nxt):
            continue
        # print("다음 방문지", bin(visited | (1 << nxt)))
        cost = dfs(nxt, visited | (1 << nxt)) + graph[now][nxt]
        min_cost = min(min_cost, cost)

    dp[(now, visited)] = min_cost
    return min_cost


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = {}

print(dfs(0, 1))
