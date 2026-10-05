def solve():
    xau = input()
    cnt4 = 0
    cnt7 = 0
    for c in xau:
        if c == '4': cnt4+=1
        if c == '7': cnt7+=1
    total = cnt4 + cnt7
    if total == 4 or total == 7:
        print("YES")
    else:
        print("NO")
solve()