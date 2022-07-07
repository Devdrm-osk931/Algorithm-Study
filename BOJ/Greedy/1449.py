import sys
si = sys.stdin.readline

n, length = tuple(map(int, input().split()))
locations = list(map(int, input().split()))
locations.sort()

start, end = -1, -1
cnt = 0

for idx in range(n):
    if locations[idx] > end:
        cnt += 1
        start = locations[idx] - 0.5
        end = length + start

print(cnt)