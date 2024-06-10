import sys
INPUT = sys.stdin.readline
# 15080번 Every Second Counts

MAX_SEC = 24 * 3600
start_time = list(map(int, INPUT().split(":")))
end_time = list(map(int, INPUT().split(":")))

start_sec = 3600 * start_time[0] + 60 * start_time[1] + start_time[2]
end_sec = 3600 * end_time[0] + 60 * end_time[1] + end_time[2]

if start_sec <= end_sec:
    print(end_sec - start_sec)
else:
    print(MAX_SEC + end_sec - start_sec)
