def solve():
    num = int(input())
    res_set=set()
    while num > 0:
        xau = input()
        res_set.add(xau)
        num-=1
    print(len(res_set))
solve()