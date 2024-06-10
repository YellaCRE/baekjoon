import sys
INPUT = sys.stdin.readline
# 31925번 APC2shake!

N = int(INPUT())
participant_list = []
for _ in range(N):
    name, isJaehak, isWinner, highScore, rank = INPUT().strip().split(" ")
    # 아주대학교 학부 소속의 재학생
    if isJaehak != 'jaehak':
        continue
    # 역대 국제 대학생 프로그래밍 경시대회(이하 ICPC)의 수상자가 아닌 자
    if isWinner == 'winner':
        continue
    # 역대 shake! 3위 이내의 수상자가 아닌 자
    if 0 < int(highScore) < 4:
        continue

    participant_list.append([name, int(rank)])

p_cnt = len(participant_list)
sorted_list = sorted(participant_list, key=lambda x: x[1])

if p_cnt > 10:
    ans_list = sorted(sorted_list[:10], key=lambda x: x[0])

    print(10)
    for i in range(10):
        print(ans_list[i][0])

else:
    ans_list = sorted(sorted_list, key=lambda x: x[0])

    print(p_cnt)
    for i in range(p_cnt):
        print(ans_list[i][0])
