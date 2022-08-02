#BOJ_9934_완전 이진트리_Silver1

depth = int(input())
preorder = list(map(int, input().split()))

floors = [
    []
    for _ in range(depth)
]

def make_tree(visit_order, layer):
    if layer == depth:
        return
    mid = len(visit_order)//2
    floors[layer].append(visit_order[mid])

    make_tree(visit_order[:mid], layer + 1)
    make_tree(visit_order[mid + 1:], layer + 1)

make_tree(preorder, 0)
for floor in floors:
    for node in floor:
        print(node, end=' ')
    print()