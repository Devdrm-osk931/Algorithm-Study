# BOJ_5639이진 검색 트리_골드5
import sys
sys.setrecursionlimit(10**6)

# 노드의 갯수가 주어지지 않은 입력을 받는다
preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(first, end):
    if first > end:
        return

    mid = end + 1  # 노드가 하나인 경우를 대비...
    for i in range(first + 1, end + 1):
        if preorder[first] < preorder[i]:
            mid = i
            break

    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(preorder[first])

postorder(0, len(preorder) - 1)