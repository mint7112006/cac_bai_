n = input().strip()
while len(n) != 1:
    limit = len(n)//2
    left = n[:limit]
    right = n[limit:]
    sum = int(left) + int(right)
    n = str(sum)
    print(n)
