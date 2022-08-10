# BOJ_11053_가장 긴 증가하는 부분 수열_Silver2
"""
- https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

"""

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

"""
LIS using Binary Search #1
LIS의 길이만을 알 수 있음...
LIS를 이루고 있는 원소를 알고싶다면 어떻게 해야하는가?
"""
import bisect

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for idx in range(n):
    if nums[idx] > dp[-1]:
        dp.append(nums[idx])
    else:
        push_idx = bisect.bisect_left(dp, nums[idx])
        dp[push_idx] = nums[idx]

print(dp)  # 이것이 실제 LIS 를 나타내지 않는다는 문제가 있다
print(len(dp))

"""
LIS SOLUTION #2
"""

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)  # LIS 길이
print(max_dp)
max_idx = dp.index(max_dp)
lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(nums[max_idx])
        max_dp -= 1
    max_idx -= 1
lis.reverse()
print(*lis)