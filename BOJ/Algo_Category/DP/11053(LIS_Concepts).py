# BOJ_11053_가장 긴 증가하는 부분 수열_Silver2

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # 현재 고려중인 숫자(i 번째 인덱스의 숫자)가 0 ~ i - 1 숫자들보다 큰 경우 추가가 가능하고, 추가되는 경우 dp[j] + 1과 기존의 값 중 큰 값을 취한다
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)

"""
- DP 방법으로 최장 증가 부분수열을 도출하는 경우 시간 복잡도가 O(n^2)이 된다.
- 더 최적화 하기 위해 이분탐색을 사용할 수 있다
  이분탐색을 사용할 경우 시간 복잡도를 n^2 => n logn 으로 줄일 수 있다.
"""