# BOJ_1991_Silver1
# 트리 순회
import sys
input = sys.stdin.readline

n = int(input())

s = [
    [0] * 3
    for _ in range(n)
]

for _ in range(n):
    node, left, right = tuple(input().split())
    item = ord(node) - 65
    s[item][0], s[item][1], s[item][2] = node, left, right


# 전위 순회: node -> left -> right
def preorder(a):
    print(a, end='')
    # node a의 lc가 존재한다면
    if s[ord(a) - 65][1] != ".":
        preorder(s[ord(a) - 65][1])
    # node a의 rc가 존재한다면
    if s[ord(a) - 65][2] != ".":
        preorder(s[ord(a) - 65][2])


# 중위 순회: left -> node -> right
def inorder(a):
    if s[ord(a) - 65][1] != ".":
        inorder(s[ord(a) - 65][1])
    print(a, end='')
    if s[ord(a) - 65][2] != ".":
        inorder(s[ord(a) - 65][2])


# 후위 순회: left -> right -> node
def postorder(a):
    if s[ord(a) - 65][1] != ".":
        postorder(s[ord(a) - 65][1])
    if s[ord(a) - 65][2] != ".":
        postorder(s[ord(a) - 65][2])
    print(a, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')