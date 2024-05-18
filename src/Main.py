import sys
sys.setrecursionlimit(int(1e9))
INPUT = sys.stdin.readline

# 2533번 사회망 서비스
N = int(INPUT())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, INPUT().split())
    graph[start].append(end)
    graph[end].append(start)

dp = [[0, 1] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True


def dfs(parent_node):
    for child_node in graph[parent_node]:
        # 아직 방문하지 않은 노드일 경우
        if not visited[child_node]:
            visited[child_node] = True
            # 일단 리프 노드까지 도착한다
            dfs(child_node)
            # 자식 노드가 없으면 return 되면서 실행되기 때문에
            # 리프 노드부터 컨텍스트 실행

            # 부모 노드가 얼리어답터가 아닌 경우, 자식 노드는 반드시 얼리어답터이다
            dp[parent_node][0] += dp[child_node][1]
            # 부모 노드가 얼리어답터인 경우, 자식노드는 상관없음(작은 수)
            dp[parent_node][1] += min(dp[child_node])


dfs(1)
print(min(dp[1]))
