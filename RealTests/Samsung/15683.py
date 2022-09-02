BLANK = 0
WALL = 6

n, m = tuple(map(int, input().split()))

map = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상태를 되돌려주기 위한 원본 데이터
copied = [
    row[:]
    for row in map
]

# 좌표 순서대로 배치된 cctv의 종류를 선정
cctvs = [
    map[i][j]
    for i in range(n)
    for j in range(m)
    if map[i][j] != BLANK and map[i][j] != WALL
]

cctv_cnt = len(cctvs)


p = []
def make_permutation(cnt):
    if cnt == cctv_cnt:
        print(p)
        return
    for i in range(4):
        p.append(i)
        make_permutation(cnt + 1)
        p.pop()

print("cctv:", cctvs)
make_permutation(0)