a = input().split()
b = {}
for i in a:
    b[i] = b.get(i, 0) + 1
c = sorted(b.items(), key = lambda item: (-item[1], item[0]))
for i, count in c:
    print(f"{i}:{count}",end=";"if i != c[-1][0] else "")

    