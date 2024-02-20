# 1987번 알파벳
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def dfs(current_row, current_col, visited: set):
    global cnt

    for i in range(4):
        nr = current_row + dr[i]
        nc = current_col + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if board[nr][nc] not in visited:
            visited.add(board[nr][nc])
            cnt = max(cnt, len(visited))
            dfs(nr, nc, visited)
            visited.remove(board[nr][nc])
    return


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

cnt = 1
visited_list = set()
visited_list.add(board[0][0])
dfs(0, 0, visited_list)

print(cnt)
