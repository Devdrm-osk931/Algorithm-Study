# BOJ 1654

# 문제 -> N개의 랜선을 만들 수 있는 랜선의 최대 길이
# 랜선의 길이는 최소 1 ~ 가장 짧은 랜선의 길이가 될것임
# 1 <= K <= 10,000
# 1 <= N <= 1,000,000
# 랜선의 길이 => 2^31 - 1 보다 작거나 같음
# 완전 탐색을 할 경우 최악 2^31 * 10,000 만큼의 시간복잡도

# 파라메트릭 서치 -> 최적화 문제를 결정 문제로 바꾸어 푸는 것
# 이분 탐색을 이용해서 mid 값을 기준으로 결정을 한다

# 마지막에 관심있는 변수가 left 인가 right인가?

# ======================================================
K, N = tuple(map(int, input().split()))
lans = [int(input()) for _ in range(K)]

left = 1
right = min(lans)

while left <= right:
    # 중앙값을 이용해서 랜선을 잘라본다
    total = 0
    mid = (left + right) // 2
    for lan in lans:
        total += lan // mid

    # total 값을 이용해서 "결정"을 한다
    if total >= N:
        left = mid + 1
    else:
        right = mid - 1


print(right)
