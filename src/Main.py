# 7579번 앱
N, M = map(int, input().split())
on_memory = list(map(int, input().split()))
off_memory = list(map(int, input().split()))
cost = sum(off_memory) + 1

dp = [[0 for _ in range(cost)] for _ in range(N)]

answer = int(1e9)

for i in range(N):
    on_current = on_memory[i]
    off_current = off_memory[i]
    for j in range(cost-1, -1, -1):
        if j >= off_current:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-off_current] + on_current)
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j])

        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)
