from collections import deque
max_score = - 1

def solution(pairs):
    global max_score
    answer = []
    tree = {}

    for parent, child in pairs:
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
    

    def bfs(root):
        score = 0
        q = deque()

        q.append((root, 0))

        while q:
            prev_node, prev_dist = q.popleft()
            if prev_dist in [1, 2, 3]:
                if prev_dist == 1:
                    score += 10
                elif prev_dist == 2:
                    score += 3
                else:
                    score += 1
            
            if prev_node in tree:
                for next_node in tree[prev_node]:
                    q.append((next_node, prev_dist + 1))
        
        return score
    
    for key in tree.keys():
        case_score = bfs(key)
        print(case_score)
        max_score = max(max_score, case_score)

            

(solution([[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]))
print(max_score)