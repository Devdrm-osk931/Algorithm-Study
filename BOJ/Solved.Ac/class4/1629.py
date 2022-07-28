#BOJ_class4_1629_silver1

# 숫자 A, B, C를 입력받는다
a, b, c = tuple(map(int, input().split()))

# 고속거듭제곱 알고리즘(분할-정복)을 통해 값을 구한다
def fast_power(base, exp, mod):
    result = 1

    while exp > 0:
        #지수가 홀수라면
        if exp % 2 != 0:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod

    print(result)

fast_power(a, b, c)