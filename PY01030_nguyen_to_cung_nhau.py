def gcd(n, num):
    while num > 0:
        mod = n % num
        n = num
        num = mod
    return n
def solve():
    w = list(map(int, input().split()))
    n = w[0]
    k = w[1]
    start1 = 10 ** (k-1)
    limit = 10 ** k
    res=[]
    for i in range (start1,limit,1):
        if gcd(n,i) == 1:
            res.append(str(i))
    result = []
    tmp=[]
    cnt = 0
    
    for i in res:
        tmp.append(i)
        cnt+=1
        if cnt == 10:
            result.append(" ".join(tmp))
            tmp=[]
            cnt = 0
    
    if tmp:
        result.append(" ".join(tmp))
    for i in result:
        print(i)
    
solve()