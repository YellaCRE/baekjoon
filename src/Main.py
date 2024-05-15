import sys
INPUT = sys.stdin.readline
DIV = 1000000009

# 15988번 1,2,3 더하기 3
T = int(INPUT())
t_list = []
for _ in range(T):
    t_list.append(int(INPUT()))
N = max(t_list)

dp = [0 for _ in range(N+1)]
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(N+1):
    for jump in [1, 2, 3]:
        if i + jump < N+1:
            dp[i+jump] += dp[i] % DIV

for t in t_list:
    print(dp[t] % DIV)
