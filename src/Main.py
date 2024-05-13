import sys
INPUT = sys.stdin.readline

# 1912번 연속합
N = int(INPUT())
num_list = list(map(int, INPUT().split()))
dp = [0 for _ in range(N)]
dp[0] = num_list[0]
for i in range(1, N):
    # 이전까지의 max 값이 dp에 저장되기 때문에 
    # 다음 값만 고려해서 max 함수를 사용하면 된다
    dp[i] = max(num_list[i], dp[i-1]+num_list[i])

# 그리고 max(dp)를 통해 이전 max 값들 중 가장 큰 값을 찾으면 된다
print(max(dp))
