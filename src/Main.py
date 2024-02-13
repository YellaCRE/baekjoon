# 1202번 보석 도둑
from heapq import heappush, heappop

N, K = map(int, input().split())
stones = []
bags = []
result = 0

for _ in range(N):
    heappush(stones, list(map(int, input().split())))

for _ in range(K):
    bags.append(int(input()))
bags_sort = sorted(bags)

# 가치 순으로 가방에 넣어야 하기 때문에 대기할 공간이 필요
candi_stone = []
# 가방을 하나씩 꺼낸다
for bag in bags_sort:
    # 적당한 크기의 보석을 모두 꺼낸다
    while stones and bag >= stones[0][0]:
        heappush(candi_stone, -heappop(stones)[1])
    # 만약 꺼내진 보석이 있다면 가장 큰 놈 하나만 pop
    if candi_stone:
        result -= heappop(candi_stone)
    # 보석이 더 이상 없으면
    elif not stones:
        break

print(result)
