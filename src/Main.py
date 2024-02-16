# 2568번 전깃줄 2
from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
line_list = []
for _ in range(N):
    line_list.append(list(map(int, input().split())))
line_list.sort(key=lambda x: x[0])

select_line_list = []
check = []
for line in line_list:
    if not select_line_list:
        select_line_list.append(line[1])
    if line[1] > select_line_list[-1]:
        select_line_list.append(line[1])
        check.append((len(select_line_list)-1, line[1]))
    else:
        index = bisect_left(select_line_list, line[1])
        select_line_list[index] = line[1]
        check.append((index, line[1]))

backtrace = []
last_index = len(select_line_list)-1
for i in range(len(check)-1, -1, -1):
    if check[i][0] == last_index:
        backtrace.append(check[i][1])
        last_index -= 1

print(N - len(backtrace))

delete_line_list = []
for line in line_list:
    if line[1] not in backtrace:
        delete_line_list.append(line[0])
delete_line_list.sort()

print(*delete_line_list, sep='\n')
