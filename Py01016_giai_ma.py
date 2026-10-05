def solve():
    t = int(input())
    while t > 0:
        xau = input()
        res=""
        for i in range(0, len(xau)-1,2):
            letter = xau[i]
            digit = int(xau[i+1])
            res+=(letter*digit)
        print(res)
        t-=1
solve()