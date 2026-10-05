n = int(input())
X = []
while n > 0:
    xau = input()
    num = 0
    flag = False
    for x in xau:
        if '0' <= x and x <= '9':
            num = num*10 + int(x)
            flag = True
        else:
            if flag: X.append(num)
            num = 0
            flag = False
    if flag:
        X.append(num)
    n-=1
X.sort()
for x in X: print(x)