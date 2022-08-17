# BOJ_22856 트리 순회_Gold4
import sys
sys.setrecursionlimit(10 ** 9)

LEAF = [-1, -1]

n = int(input())
tree = {}
for _ in range(n):
    a, b, c = tuple(map(int, input().split()))
    tree[a] = [b, c]


ans = 0
root_to_leaf = 0

def similar_traverse(root, depth):
    global ans, root_to_leaf

    # print(root)
    ans += 1

    if tree[root] == LEAF:
        root_to_leaf = depth
        return
    
    similar_traverse(tree[root][0], depth + 1)
    # print(root)
    ans += 1

    if tree[root][1] != -1:
        similar_traverse(tree[root][1], depth + 1)
        # print(root)
        ans +=1
    


similar_traverse(1, 0)
print(ans - root_to_leaf - 1)