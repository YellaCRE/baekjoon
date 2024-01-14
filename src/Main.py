from itertools import combinations
# 2798번 블랙잭

N, M = map(int, input().split())
cards = list(map(int,input().split()))

res = 0
for combi in combinations(cards, 3):
    temp = sum(combi)
    if temp > M:
        continue
    res = max(res, sum(combi))

print(res)
