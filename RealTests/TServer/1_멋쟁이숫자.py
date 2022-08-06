def solution(s):
    if len(s) < 3:
        return -1
    
    ans = -1
    for idx in range(0, len(s) - 2):
        if s[idx:idx + 3] == s[idx] * 3:
            ans = max(ans, int(s[idx:idx + 3]))     
    
    return ans

print(solution("12223"))
print(solution("111999333"))
print(solution("123"))