max_count = 0
def dfs(word_dict, target, result, cnt):
    global max_count
    if result == target:
        max_count = max(max_count, cnt)
        return result
    if len(result) > len(target):
        return

    for word in word_dict:
        if result == "":
            if target[0] == word[0]:
                dfs(word_dict, target, result + word, cnt + 1)
        else:
            if result[-1] == word[0]:
                dfs(word_dict, target, result + word[1:], cnt + 1)


def solution(s, word_dict):
    global max_count
    dfs(word_dict, s, "", 0)
    return max_count