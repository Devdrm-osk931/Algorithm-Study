# Codetree
# 삼성 SW 역량테스트 2015 하반기 2번

# Variables
OUT_OF_MAP = (n, m)

tc = int(input())

for _ in range(tc):
    n, m = tuple(map(int, input().split()))

    graph = [
        list(input())
        for _ in range(n)
    ]

    

# Functions

# 격자에 파란 구슬이 남아있는지 확인
def blue_exists(blue_pos):
    return blue_pos != OUT_OF_MAP