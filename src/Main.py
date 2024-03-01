# 2166번 다각형의 면적

N = int(input())
point_list = []
for i in range(N):
    point_list.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    if i == N-1:
        ans += (point_list[i][0] * point_list[0][1]) - (point_list[0][0] * point_list[i][1])
    else:
        ans += (point_list[i][0] * point_list[i+1][1]) - (point_list[i+1][0] * point_list[i][1])

print(round(abs(ans)*0.5, 1))
