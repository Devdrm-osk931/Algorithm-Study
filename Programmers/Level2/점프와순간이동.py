# Programmers
# 점프와 순간이동

def solution(n):
    ans = 0

    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

        if n == 0:
            return ans
