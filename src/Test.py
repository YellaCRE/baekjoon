import sys
INPUT = sys.stdin.readline
DIV = 1000000009

# 15988번 1,2,3 더하기 3
T = int(INPUT())
t = []
for _ in range(T):
    t.append(int(INPUT()))

t_sort = set(t)
t_d = {1: 1, 2: 2, 3: 4}

j = 0
a, b, c = 1, 2, 4
for i in range(4, 1000010):
    # 피보나치 수열과 같은 규칙이 존재
    c, b, a = (a + b + c) % int(1e9 + 9), c, b
    if i in t:
        t_d.update({i: c})
        j += 1
        if j == t:
            break

for i in t:
    print(t_d[i])
