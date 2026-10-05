def check1(xau):
    if xau[0] == xau[1] or len(xau) % 2 == 0:
        return 0
    else:
        return 1
    
#Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
def check2(xau):
    tmp = xau[0]
    for i in range(0,len(xau),2):
        if xau[i] != tmp:
            return 0
    return 1
def solve():
    t = int(input())
    while t > 0:
        xau = input()
        if check1(xau) and check2(xau):
            print("YES")
        else:
            print("NO")
        t-=1
solve()