def sum(num):
    xau = str(num)
    rev_num = xau[::-1]
    return num + int(rev_num)
def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        cnt = 0
        total = n
        flag = 0
        
        while True:
            if total % 7 == 0 or cnt > 1000:
                flag = 1
                break
            total = sum(total) 
            cnt+=1
        if flag:
            print(total)
        else:
            print("-1")
        t-=1
solve()