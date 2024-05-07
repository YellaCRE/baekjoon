import sys
input = sys.stdin.readline

# 29790번 임스의 메이플컵
N, U, L = map(int, input().split())

if N < 1000:
    print("Bad")
elif U >= 8000 or L >= 260:
    print("Very Good")
else:
    print("Good")

