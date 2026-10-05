def solve():
    t = int(input())
    while t > 0:
        xau = input()
        res=""
        for i in range(0,len(xau)-1,2):
            chu = xau[i]
            num = int(xau[i+1])
            res+= (chu*num)
        print(res)
        t-=1
        
solve()