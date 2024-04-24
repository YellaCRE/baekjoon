# 1103번 게임
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def is_in_range(r, c):
    return 0 <= r < N and 0 <= c < M


def coin_move(r, c):
    if visited[r][c]:
        print(-1)
        exit()
    visited[r][c] = True

    move_dist = int(board[r][c])
    for d in range(4):
        nxt_row, nxt_col = r + move_dist * dr[d], c + move_dist * dc[d]

        if not is_in_range(nxt_row, nxt_col):
            continue

        if board[nxt_row][nxt_col] == 'H':
            continue

        if dp[r][c]+1 <= dp[nxt_row][nxt_col]:
            continue

        dp[nxt_row][nxt_col] = dp[r][c] + 1
        coin_move(nxt_row, nxt_col)

    visited[r][c] = False
    return


N, M = map(int, input().split())
dp = [[0 for _ in range(M)] for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(input()))

visited = [[False for _ in range(M)] for _ in range(N)]
coin_move(0, 0)

answer = 0
for dp_item in dp:
    answer = max(answer, max(dp_item))
print(answer + 1)
