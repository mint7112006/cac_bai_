import math
def solve():
    t = int(input())
    while t > 0:
        num = int(input())
        cnt = 0
        for i in range(2, int(math.sqrt(2*num))+1, 1):
            if (2*num) % i == 0:
                m = (2*num)//i
                if m != i and (m-i+1) % 2 == 0:
                    cnt+=1
        print(cnt)
        t-=1
solve()