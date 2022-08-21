#BOJ_Class4_10830_행렬 제곱_Gold4

# 고속 거듭제곱 알고리즘 뢰직을 사용하면 보다 효율적으로 해결할 수 있을것 같다

n, b = tuple(map(int, input().split()))

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]



