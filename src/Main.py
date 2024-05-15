import sys
INPUT = sys.stdin.readline
MAX_TIME = 15 * 60

# 29792번 규칙적인 보스돌이
N, M, K = map(int, INPUT().split())

damage_list = []
for _ in range(N):
    damage_list.append(int(input()))

# 공격력 순 정렬, 강한 M개의 캐릭터 사용
damage_list.sort(reverse=True)

# [보스의 체력, 드랍하는 메소]
boss_list = []
for _ in range(K):
    boss_list.append(list(map(int, input().split())))


def maxMeso(d):
    dp = [0] * (MAX_TIME + 1)
    for hp, value in boss_list:
        # 보스를 잡기 위해 걸리는 시간
        time = (hp + d - 1) // d
        # 만약 15분 이내에 잡을 수 없다면 continue
        if MAX_TIME < time:
            continue

        for j in range(MAX_TIME, 0, -1):
            if j - time >= 0 and dp[j - time] != 0:
                dp[j] = max(dp[j], dp[j - time] + value)

        dp[time] = max(dp[time], value)

    return max(dp)


total_coin = 0
# M개의 캐릭터 사용
for i in range(M):
    total_coin += maxMeso(damage_list[i])

print(total_coin)
