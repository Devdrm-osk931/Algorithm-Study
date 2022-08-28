# Samsung
# 14889 스타트와 링크 (Silver2)

n = int(input())

synergy = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_diff = 1e9

people = [i for i in range(n)]
start = []

# idx번째 요소를 start 팀에 배치하는 함수
def pick_start(cnt, idx):
    if cnt == n//2:
        print(start)
        return

    if idx == n:
        return

    start.append(idx)
    for i in range(idx + 1, n):
        pick_start(cnt + 1, i)
    start.pop()

pick_start(0, 0)