def solve():
    t = int(input())
    cnt = 0
    while t > 0:
        cnt+=1
        s1 = input()
        s2 = input()
        
        flag = 1
        if len(s1) != len(s2):
            flag = 0
        for i in s2:
            if s1.count(i,0,len(s1)) != s2.count(i,0,len(s2)):
                flag = 0
        
        if flag:
            print(f"Test {cnt}: YES")
        else:
            print(f"Test {cnt}: NO")
        t-=1
solve()