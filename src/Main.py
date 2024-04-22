# 1049번 기타줄
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bundle_string = int(1e9)
single_string = int(1e9)
for _ in range(M):
    bundle_price, single_price = map(int, input().split())
    bundle_string, single_string = min(bundle_string, bundle_price), min(single_string, single_price)

answer = 0
if single_string * 6 <= bundle_string:
    answer = single_string * N
else:
    bundle_cnt = N // 6
    mod = N % 6
    answer += bundle_cnt * bundle_string
    if mod * single_string > bundle_string:
        answer += bundle_string
    else:
        answer += mod * single_string

print(answer)