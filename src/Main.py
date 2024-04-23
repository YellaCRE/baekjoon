# 11000번 강의실 배정
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
q = []

for i in range(N):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heappush(room, q[0][1])

for i in range(1, N):
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heappush(room, q[i][1])

print(len(room))
