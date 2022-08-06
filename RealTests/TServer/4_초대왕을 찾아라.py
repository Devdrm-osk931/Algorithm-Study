from collections import deque

def solution(invitationPairs):
    answer = []

    tree = {}
    scores = {}

    for parent, child in invitationPairs:
        if parent not in tree:
            tree[parent] = [child]
            scores[parent] = 0
        else:
            tree[parent].append(child)

    def compute_score(root, depth, score):
        if depth == 3:
            return score
        
        if root in tree:
            if depth == 0:
                score += 10 * len(tree[root])
            elif depth == 1:
                score += 3 * len(tree[root])
            else:
                score += len(tree[root])
            
            for next_node in tree[root]:
                return compute_score(next_node, depth + 1, score)
        
    for root in tree.keys():
        scores[root] = compute_score(root, 0, 0)
        print(scores[root])
    return answer

print(solution([[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]))