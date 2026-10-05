def check(xau):
    for i in xau:
        if i != '4' and i != '7':
            return 0
    return 1
def solve():
    t = int(input())
    while True:
        xau = input()
        if not check(xau):
            print("Nhap lai:")
        else:
            print(xau)
            break

solve()