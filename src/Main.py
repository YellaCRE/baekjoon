# 9406번 텀 프로젝트
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def find_team(i):
    global result
    visited[i] = True
    cycle.append(i)

    nxt_member = team_select[i]
    if visited[nxt_member]:
        if nxt_member in cycle:
            start_idx = cycle.index(nxt_member)
            result += cycle[start_idx:]
        return
    else:
        find_team(nxt_member)


T = int(input())
for _ in range(T):
    N = int(input())
    team_select = list(map(int, input().split()))
    team_select.insert(0, 0)
    visited = [False for _ in range(N+1)]
    result = []

    for idx in range(1, N+1):
        if not visited[idx]:
            cycle = []
            find_team(idx)

    print(N - len(result))
