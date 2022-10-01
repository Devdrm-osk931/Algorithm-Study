n = int(input())
nums = list(map(int, input().split()))

NGE = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        NGE[stack.pop()] = nums[i]
    stack.append(i)
print(NGE)