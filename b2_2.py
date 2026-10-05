def solve():
    t = int(input())
    while t > 0:
        xau = input()
        if xau[0] == xau[len(xau)-1]:
            print("YES")
        else:
            print("NO")
        t-=1
solve()