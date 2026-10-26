stones = input().strip()
jewels = input().strip()
b = 0
for i in stones:
    if i in jewels:
        b += 1
print(b)