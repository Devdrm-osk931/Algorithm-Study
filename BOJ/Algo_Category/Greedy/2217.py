# BOJ_2217_로프_실버4

# 로프의 갯수
n = int(input())

# 로프 정보
ropes = [
    int(input())
    for _ in range(n)
]

ropes.sort(reverse=True)
ans = 0
for i, rope in enumerate(ropes, start=1):
    ans = max(ans, i*rope)

print(ans)