import sys
from math import ceil, log2

sys.setrecursionlimit(int(1e8))
INPUT = sys.stdin.readline
MAX = int(1e9)
MIN = 0

# 2357번 최솟값과 최댓값
N, M = map(int, INPUT().split())
num_list = []
for _ in range(N):
    num_list.append(int(INPUT()))

answer_range = []
for _ in range(M):
    answer_range.append(list(map(int, INPUT().split())))

# 세그먼트 트리 크기 구하기
h = ceil(log2(len(num_list))) + 1
nodeNum = 2 ** h
seg_tree = [[0, 0] for _ in range(nodeNum)]


def makeSegTree(idx, start, end):
    # 만약 리프노드이면
    if start == end:
        seg_tree[idx] = [num_list[start], num_list[start]]
        return seg_tree[idx]

    mid = (start + end) // 2
    left = makeSegTree(idx * 2, start, mid)
    right = makeSegTree(idx * 2 + 1, mid + 1, end)
    
    # 자식의 값 중 min, max 값을 부모 노드에 저장한다
    seg_tree[idx] = [min(left[0], right[0]), max(left[1], right[1])]
    return seg_tree[idx]


def find(idx, find_start, find_end, start, end):
    if end < find_start or find_end < start:
        return [int(1e9), 0]

    if find_start <= start and end <= find_end:
        return seg_tree[idx]

    mid = (start + end) // 2
    left = find(idx * 2, find_start, find_end, start, mid)
    right = find(idx * 2 + 1, find_start, find_end, mid + 1, end)
    
    return [min(left[0], right[0]), max(left[1], right[1])]


makeSegTree(1, 0, len(num_list) - 1)

for answer_start, answer_end in answer_range:
    print(*find(1, answer_start-1, answer_end-1, 0, len(num_list) - 1))
