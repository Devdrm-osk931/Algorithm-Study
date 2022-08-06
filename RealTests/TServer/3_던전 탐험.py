# Programmers
def solution(k, dungeons):
    case = []
    l = len(dungeons)
    answer = -1


    def make_permutation(depth, dungeons):
        nonlocal answer
        if depth == l:
            case_cnt = 0
            have = k
            for need, use in case:
                if need > have:
                    break
                case_cnt += 1
                have -= use
            answer = max(answer, case_cnt)
            return
        else:
            for i in range(len(dungeons)):
                case.append(dungeons[i])
                make_permutation(depth + 1, dungeons[:i] + dungeons[i + 1:])
                case.pop()
    
    make_permutation(0, dungeons)

    return answer