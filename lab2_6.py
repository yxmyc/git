nums = list(map(int, input().split()))
a = sorted(set(nums))[::-1]
if len(a) < 3:
    print(a[0])
else:
    print(a[2])