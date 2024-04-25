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
        # 만약 visited인데 사이클에 없으면 그 멤버는 어느 프로젝트 팀에도 속할 수 없다
        # 이미 visited라는 뜻은 선택권을 사용했다는 의미, 만약 선택권을 사용했는데 선택받지 못했다면 다른 경우의 수는 나올 수 없다
        if nxt_member in cycle:
            start_idx = cycle.index(nxt_member)
            # 리스트를 더하기 연산하면 펼쳐서 값을 append 할 수 있다
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
