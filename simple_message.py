def twoSum(sorted_nums,target):
    left = 0
    right = len(sorted_nums) - 1
    while left < right:
        current_sum = sorted_nums[left] + sorted_nums[right]
        if current_sum == target:
            print([left, right])
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1
nums = [2, 7, 3, 6]
sorted_nums = sorted(nums)
target = 9
twoSum(sorted_nums, target)