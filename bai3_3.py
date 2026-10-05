def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        num1 = sorted(map(int, input().split()))
        num2 = sorted(map(int, input().split()))
        
 
        flag = 1
        for i in range(n):
            if num1[i] > num2[i]:
                flag = 0
                break
        if flag == 1:
            print("YES")
        else:
            print("NO")
        t-=1
solve()