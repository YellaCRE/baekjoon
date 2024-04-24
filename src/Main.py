# 1103번 게임(개선)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def is_in_range(r, c):
    return 0 <= r < N and 0 <= c < M


def coin_move(r, c, cnt):
    global result
    result = max(result, cnt)

    move_dist = int(board[r][c])
    for d in range(4):
        nxt_row, nxt_col = r + move_dist * dr[d], c + move_dist * dc[d]

        if not is_in_range(nxt_row, nxt_col):
            continue

        if board[nxt_row][nxt_col] == 'H':
            continue

        if dp[r][c]+1 <= dp[nxt_row][nxt_col]:
            continue

        if visited[nxt_row][nxt_col]:
            print(-1)
            exit()

        dp[nxt_row][nxt_col] = cnt + 1
        visited[nxt_row][nxt_col] = True
        coin_move(nxt_row, nxt_col, cnt+1)
        visited[nxt_row][nxt_col] = False


result = 0
N, M = map(int, input().split())
dp = [[0 for _ in range(M)] for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(input()))

visited = [[False for _ in range(M)] for _ in range(N)]
coin_move(0, 0, 0)

print(result + 1)
