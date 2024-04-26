# 1058번 친구
import sys
input = sys.stdin.readline


N = int(input())
friends = [list(input()) for _ in range(N)]

connected = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # 두 사람이 친구이거나 A와 친구이고, B와 친구인 C가 존재해야한다
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                connected[i][j] = 1

answer = 0
for row in connected:
    # 한 사람의 친구의 수는 sum(row)
    answer = max(answer, sum(row))

print(answer)
