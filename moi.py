def solve():
    t = int(input())
    ds = []
    for _ in range(t):
        tmp=[]
        tmp.append(input().strip())
        tmp.append(input().strip())
        tmp.append(input().strip())
        tmp.append(int(10))
        ds.append(tmp)
    
    for _ in range(t):
        msv, dd = map(str, input().split())
        vtri = 0
        for i in range(t):
            if msv == ds[i][0]:
                vtri = i
                break
        for kt in dd:
            if kt == 'v':
                ds[vtri][3] -=2
            elif kt == 'm':
                ds[vtri][3] -=1
    
    for i in range(t):
        if ds[i][3] <= 0:
            ds[i][3] = 0
            for j in range(len(ds[i])):
                print(ds[i][j], end=" ")
            print("KDDK")
        else:
            for j in range(len(ds[i])):
                print(ds[i][j], end=" ")
            print()
solve()          