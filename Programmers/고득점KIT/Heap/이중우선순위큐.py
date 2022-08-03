import heapq

"""
이전에 백준에서 해당 문제를 풀었을 땐, 힙에 추가해준 각 요소에 key값을 부여하여 해당 원소가 삭제 됐는지에 대한 여부를 확인했었으나,
heap의 remove 내장 메서드를 사용하니 보다 편리하게 구현이 가능하였음... 백준이 시간이 더 깐깐한 편이라서 아래처럼 구현하면 시간적으로 불리할수도 있을 것 같음

최소 힙 하나만을 사용하면서도 해결이 가능한데, heapq.nlargest(n, iterable, key) 내장 메서드를 이용하는것이다
최소 힙을 사용하더라도 해당 메서드를 통해 가장 큰 n개의 요소를 뽑기가 가능하고, 슬라이싱을 통해 1번 인덱스부터 추출한다면 최댓값을 삭제한 효과를 가져올 수 있다.
"""


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        cmd = operation.split()
        target = int(cmd[1])
        if cmd[0] == 'I':
            heapq.heappush(min_heap, target)
            heapq.heappush(max_heap, (-target, target))
        else:
            if target == 1:
                if not max_heap:
                    continue
                max_value = heapq.heappop(max_heap)[1]
                min_heap.remove(max_value)
            else:
                if not min_heap:
                    continue
                min_value = heapq.heappop(min_heap)
                max_heap.remove((-min_value, min_value))

    if min_heap:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0, 0]





print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))