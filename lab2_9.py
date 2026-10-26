flowerbed = list(map(int, input().split()))
n = int(input())
a = 0
b = len(flowerbed)
for i in range(b):
    l = (i == 0)or(flowerbed[i - 1] == 0)
    r = (i == b - 1)or(flowerbed[i + 1] == 0)
    c = flowerbed[i] == 0
    if l and r and c:
        a += 1
        flowerbed[i] = 1
print(a >= n)