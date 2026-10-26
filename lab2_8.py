arr = list(map(int, input().split()))
a = 1
b = 0
while a <= len(arr):
    for i in range(len(arr) - a + 1):
        b += sum(arr[i : i + a])
    a += 2
print(b)