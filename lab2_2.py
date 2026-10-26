nums = list(map(int, input().split()))
n = len(nums) // 2
result = []
for i in range(n):
    result.append(nums[i])
    result.append(nums[i+n])
print(result)