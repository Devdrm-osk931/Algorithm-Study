# Codetree
# 삼성 SW 역량테스트 2015 하반기 2번

tc = int(input())

for _ in range(tc):
    n, m = tuple(map(int, input().split()))

    graph = [
        list(input())
        for _ in range(n)
    ]