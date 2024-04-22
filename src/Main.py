# 1026번 보물
import sys
input = sys.stdin.readline

answer = 0
N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()

for idx in range(N):
    B_max = max(B_list)
    answer += B_max * A_list[idx]
    B_list.remove(B_max)

print(answer)
