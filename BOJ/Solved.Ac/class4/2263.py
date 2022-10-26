# BOJ 2263
# 트리의 순회
# 원래 코드: http://colorscripter.com/s/jc1IvM7

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeIdx = dict()

for idx, item in enumerate(inorder):
    nodeIdx[item] = idx


def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return

    root = postorder[postEnd]

    left = nodeIdx[root] - inStart
    right = inEnd - nodeIdx[root]

    print(root, end=' ')
    preorder(inStart, inStart + left - 1, postStart, postStart + left - 1)
    preorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)


preorder(0, n - 1, 0, n - 1)