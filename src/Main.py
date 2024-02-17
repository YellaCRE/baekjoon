# 1644번 소수의 연속합
import sys
input = sys.stdin.readline


def prime_list(number):
    # 자기 자신도 포함
    n = number+1

    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


N = int(input())
cnt = 0
start = 0
end = 0
primes = prime_list(N)
if N != 1:
    current = primes[0]
else:
    current = -1

while start <= end:
    if current == -1:
        break

    if current == N:
        cnt += 1
        current -= primes[start]
        start += 1
    elif current < N:
        if end == len(primes)-1:
            break
        end += 1
        current += primes[end]
    else:
        current -= primes[start]
        start += 1

print(cnt)
