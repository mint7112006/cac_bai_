import math
def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n))+1,1):
        if n % i == 0:
            return 0
    return 1

def lcd(a,b):
    while b > 0:
        mod = a % b
        a = b
        b = mod
    return a
def total(n):
    sum = 0
    while n > 0:
        sum+=n % 10
        n //= 10
    return sum

def solve():
    t = int(input())
    while t > 0:
        num = list(map(int,input().split()))
        a = num[0]
        b = num[1]
        gcd = lcd(a,b)
        if snt(total(gcd)):
            print("YES")
        else:
            print("NO")
        t-=1
solve()