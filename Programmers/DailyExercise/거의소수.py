# BOJ_1456_Silver1

# 첫 시도, 잘못짰음
# 에라토스테네스의 체를 적용한답시고 짜 보았지만
# 에라토스테네스의 체의 이점을 전혀 사용하지 못하고 그냥 is_prime으로 판별한것과 다름없음
# 시간초과!!
'''
from math import sqrt

def is_prime(n):
    for div in range(2, int(sqrt(n)) + 1):
        if n % div == 0:
            return False
    return True

a, b = tuple(map(int, input().split()))
cnt = 0

# 1 ~ sqrt(b) 까지의 소수를 구한다
upper = int(sqrt(b))
prime_number = [False] * (upper + 1)

prime_number[1] = False

# 에라토스테네스의 체 --> ~ sqrt(b)까지의 소수를 구한다
for i in range(2, upper + 1):
    if is_prime(i):
        prime_number[i] = True

        # 소수들의 거듭제곱 꼴이 a ~ b 범위 안에 있다면 cnt 값을 올리고 i 값을 한번 더 곱해주며 거듭제곱한다.
        # b 보다 커진다면 루프 탈출
        k = i
        while True:
            k *= i
            if a <= k <= b:
                cnt += 1
            
            elif k > b:
                break

        for k in range(i + i, upper + 1, i):
            prime_number[k] = False

        
print(cnt)
'''

# 가장 기본적인 소수 판별 알고리즘 - O(N)

# 루트(n)까지의 숫자를 확인해봄으로써 소수를 판별할 수 있음 - O(N^(1/2))
"""
def isPrimeNumber(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""

"""
여러 숫자 또는 범위 내에 존재하는 숫자에 대한 소수 여부를 판별하기 위해선 에라토스테네스의 체 알고리즘 효과적
2부터 시작하여 자신을 제외한 배수들을 지워나간다
지운 뒤 숫자를 하나 증가시켜 동일한 과정을 반복한다
이미 지워진 숫자는 건너 뛴다
"""

from math import sqrt

a, b = tuple(map(int, input().split()))

upper = int(sqrt(b))
# 1 ~ sqrt(b) 까지의 소수를 모두 찾는다
prime = [True] * (int(sqrt(b)) + 1)
prime[0] = False
prime[1] = False
prime[2] = True

curr = 2

while curr * curr <= b:
    if not prime[curr]:
        curr += 1
        continue
    for t in range(2 * curr, upper + 1, curr):
        prime[t] = False
    curr += 1

cnt = 0
for check in range(2, upper + 1):
    if not prime[check]: continue
    mul = check * check
    
    while mul <= b:
        cnt += (a <= mul)
        mul *= check

print(cnt)