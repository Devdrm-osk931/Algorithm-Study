# BOJ 나무 자르기와 동일한 문제인것 같음
import sys
si = sys.stdin.readline

n, m = tuple(map(int, si().split()))
trees = list(map(int, si().split()))

low, high = 0, max(trees)


# trees 배열을 높이 h로 잘랐을 때 결과를 반환하는 함수
def compute_remainder(trees, h):
    global result
    result = 0
    for tree in trees:
        if tree > h:
            result += tree - h
    return result


ans = 0
while low <= high:
    mid = (low + high) // 2

    result = compute_remainder(trees, mid)
    if result >= m:
        low = mid + 1
        ans = mid

    else:
        high = mid - 1

print(ans)
