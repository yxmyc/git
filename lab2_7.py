nums = list(map(int, input().split()))
target = int(input())
a = 0
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i] + nums[j] < target:
            a += 1
print(a)