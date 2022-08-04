"""
시간초과
heap보다 빠르게 문제를 풀어야함...
"""
# #BOJ_11003_최솟값 찾기_Gold1
# import heapq
# from collections import deque
#
# N, L = tuple(map(int, input().split()))
# nums = list(map(int, input().split()))
# d_nums = deque(nums)
#
# # Compute Di ==> nums(i-L+1) ~ Ai
# for i in range(1, N + 1):
#     lb = i - L  # 0보다 작은 인덱스라면 무시하고 0부터 계산해야하는것
#     ub = i - 1
#
#     if lb < 0:
#         lb = 0
#
#     temp = list(nums)[lb: ub + 1]
#     print(str(temp) + "-->" + str(min(temp)))
#     # heapq.heapify(temp)
#     # print(temp[0],end=' ')
# print("==========================")
#
# min_heap = []
# cnt = 0
# del_idx = 0  # 0 ~ 8
# while d_nums:
#     elem = d_nums.popleft()
#     heapq.heappush(min_heap, elem)
#     print(min_heap,"-->",min_heap[0])
#     cnt += 1
#     if cnt >= L:
#         min_heap.remove(nums[del_idx])
#         heapq.heapify(min_heap)
#         del_idx += 1

"""
deque만을 사용해서 숫자들을 오름차순으로 관리할 수 있는 방법
**아이디어**
순차적으로 숫자를 데크에 넣어주는데, 이때 기존의 숫자들을 유지할지 말지 선택을 해준다
새로 들어오는 숫자는 필연적으로 데크에 가장 오래 남아있게 된다 -> 슬라이딩 윈도우
그렇다면 새로 들어온 숫자보다 큰 숫자는 항상 고려 대상에서 제외될 수 밖에 없다 - 최소값을 구할건데 가장 최근에 추가된 숫자가 더 작으므로
따라서 리스트의 요소를 단 한번 순회하며 데크에 추가해주기 전 두가지를 작업해준다.
1. 새로 추가되는 요소보다 큰 요소는 pop을 해준다
2. 슬라이딩 윈도우를 벗어나는 요소는 popleft를 해준다
"""

from collections import deque
import sys
input = sys.stdin.readline

n, l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

q = deque()

for i in range(n):
    while q and q[-1][0] > arr[i]:
        q.pop()
    while q and q[0][1] < i - l + 1:
        q.popleft()
    q.append((arr[i], i))

    print(q[0][0], end=' ')