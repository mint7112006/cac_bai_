def solve():
    t = int(input())
    while t > 0:
        xau = input()
        num1 = xau[0:2]
        l = len(xau)
        num2 = xau[l-2:]
        if num1 == num2:
            print("YES")
        else:
            print("NO")
        t-=1
solve()