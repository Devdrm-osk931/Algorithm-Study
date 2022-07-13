# 문제 설명
# 정렬된 배열이 주어질 때 특정 원소의 갯수를 구하여라
# 단 O(log N) 시간 복잡도 요구 --> 이진 탐색을 통한 lower, upper bound
# Sol1) 이진 탐색 두번 시행하여 하한선과 상한선을 구함
# Sol2) bisect 사용
# 만약 원소가 하나도 없다면 -1 을 출력한다

"""
SOLUTION #1
By using binary search twice in order to find lower and upper bound
"""

import sys
si = sys.stdin.readline

n, x = tuple(map(int, si().split()))  # N과 target 숫자가 주어짐
numbers = list(map(int, si().split()))  # 오름차순으로 정렬된 리스트가 주어진다

lower, upper = sys.maxsize, -sys.maxsize

# find index of lower bound
start, end = 0, len(numbers) - 1
while start <= end:
    mid = (start + end) // 2

    if numbers[mid] >= x:
        if numbers[mid] == x:
            lower = mid
        end = mid - 1

    else:
        start = mid + 1

# find index of upper bound
start, end = 0, len(numbers) - 1
while start <= end:
    mid = (start + end) // 2

    if numbers[mid] <= x:
        if numbers[mid] == x:
            upper = mid
        start = mid + 1

    else:
        end = mid - 1

if upper == -sys.maxsize or lower == sys.maxsize:
    print(-1)
else:
    print(upper - lower)


"""
SOLUTION #2
By using bisect library in order to find lower and upper bound

from bisect import bisect_left, bisect_right

n, x = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))

lower_bound = bisect_left(numbers, x)
upper_bound = bisect_right(numbers, x)

cnt = upper_bound - lower_bound
print(cnt if cnt > 0 else -1)
"""
