import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
INPUT = sys.stdin.readline


def getSubSequence(arr, sumArr):
    for cnt in range(1, len(arr)+1):
        for combiSum in combinations(arr, cnt):
            sumArr.append(sum(combiSum))


def getNumCnt(arr, find):
    # 찾는 숫자가 여러 개일 수 있다
    return bisect_right(arr, find) - bisect_left(arr, find)


# 1208번 부분수열의 합 2
N, S = map(int, INPUT().split())
num_list = list(map(int, INPUT().split()))

left, right = num_list[:N//2], num_list[N//2:]
left_sum, right_sum = [], []

getSubSequence(left, left_sum)
getSubSequence(right, right_sum)
# 정렬을 하는 이유는 bisect를 통해 개수를 구할 것이라
left_sum.sort()
right_sum.sort()

ans = 0
for le in left_sum:
    find_num = S - le
    # find_num 의 개수 찾기
    ans += getNumCnt(right_sum, find_num)

ans += getNumCnt(left_sum, S)
ans += getNumCnt(right_sum, S)

print(ans)
