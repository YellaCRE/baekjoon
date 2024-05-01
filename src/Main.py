# 1101번 카드 정리 1
N, M = map(int, input().split())
box_list = []
for _ in range(N):
    box_list.append(list(map(int, input().split())))

# 그냥 n 개의 상자를 전부 한번씩 조커 상자라고 가정을 해볼 수 있는 것
# 상자 속 카드를 옮길 때 어떤 카드를 어디로 옮길지 전혀 생각할 필요가 없다.
# 우리에게는 만능짬통 조커 상자가 있기 때문에 조커에 다 때려박으면 된다.

min_cnt = int(1e9)
for current_joker_idx in range(N):
    visited = [False for _ in range(M+1)]
    temp_cnt = 0
    for box_idx in range(N):
        if box_idx == current_joker_idx:
            continue

        box_flag = []
        for box_check_idx in range(len(box_list[box_idx])):
            if box_list[box_idx][box_check_idx] > 0:
                box_flag.append(box_check_idx)

        flag_cnt = len(box_flag)
        if flag_cnt == 0:
            continue
        elif flag_cnt == 1:
            if visited[box_flag[0]]:
                temp_cnt += 1
            else:
                visited[box_flag[0]] = True
        else:
            temp_cnt += 1

    min_cnt = min(min_cnt, temp_cnt)

print(min_cnt)
