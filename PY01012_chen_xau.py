def solve():
    xau1 = input()
    xau2 = input()
    index = int(input())-1
    # DO NGƯỜI TA TÍNH TỪ 1
    #[:p] từ 0 đến p-1
    #[p:] từ p trở lên
    res = xau1[:index]+xau2+xau1[index:]
    print(res)
solve()