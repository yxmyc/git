hours = list(map(int, input().split()))
target = int(input())
a = 0
for i in hours:
    if (target - i) <= 0:
        a += 1
print (a)
                