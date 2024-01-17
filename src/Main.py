# 2293번 동전 1

N, K = map(int, input().split())
coins = []
dp = [0 for _ in range(K+1)]
dp[0] = 1

for i in range(N):
    temp = int(input())
    coins.append(temp)

for coin in coins:
    for i in range(K+1):
        temp = i-coin
        if temp >= 0:
            dp[i] += dp[temp]

print(dp[-1])