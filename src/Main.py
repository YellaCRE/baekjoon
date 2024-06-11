import sys
INPUT = sys.stdin.readline
# 27466번 그래서 대회 이름 뭐로 하죠


def solve():
    last_word = ''
    double_A_flag = False

    last_idx = -1
    # 맨 뒷글자가 알파벳 자음
    for j_idx in range(N-1, 0, -1):
        if input_str[j_idx] not in ['A', 'E', 'I', 'O', 'U']:
            last_idx = j_idx
            last_word = input_str[j_idx]
            break

    if last_word == '':
        print('NO')
        return

    for j_idx in range(last_idx-1, 0, -1):
        if input_str[j_idx] == 'A':
            last_idx = j_idx
            break

    for j_idx in range(last_idx-1, 0, -1):
        if input_str[j_idx] == 'A':
            last_idx = j_idx
            double_A_flag = True
            break

    if not double_A_flag:
        print('NO')
        return

    if last_idx < M-3:
        print('NO')
        return

    print('YES')
    print(input_str[last_idx-(M-3):last_idx]+'AA'+last_word)


N, M = map(int, INPUT().split())
input_str = INPUT()
solve()
